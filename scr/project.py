import numpy as np
import matplotlib.pyplot as plt

'''

Simulation parameters and prepared function calls are in the bottom of the program

'''


def Euler_Maruyama(x0, u, h, T, D, N):
    '''
    x0 - starting position 
    u  - velocity field
    h  - time step
    T  - simulation time
    D  - diffusion coefficient
    N  - number of particles
    '''

    ''' prepares arrays and changes u and x0 to matrixes '''
    X_N = np.zeros([2, 1, N]) # array containing the position of all particles at every time step
    X = np.tile(x0, (1, N)) # generates array of stacked x0-vectors
    X_N[:,0,:] = X
    u = np.swapaxes(np.tile(u, (N, 1)), axis1=1, axis2=0) # generates array of stacked u-vectors
    n_step = 0
    while n_step*h < T:
        ''' main simulation step with random numbers for diffusion in Z and new_X is the next position of all particles added to X_N '''
        Z = np.random.normal(0, 1, (2, N)) # random number for diffusion
        new_X = X_N[:,n_step,:] + u*h + np.sqrt(2*D*h)*Z # simulation of movement
        new_X = np.expand_dims(new_X, 1) # adds dimension for stacking arrays
        X_N = np.hstack((X_N, new_X)) # appends new position to total matrix
        n_step += 1 # increments step counter
    return X_N
'''
X_N is a three dimensional array
1: Spacial dimensions (in this case 2)
2: Time step
3: Particle number
'''



def particle_cloud(x0, u, h, plot_times, D, N):
    ''' runs simulation and loops through plot times '''
    X = Euler_Maruyama(x0, u, h, max(plot_times), D, N) # runs simulation 
    t = (plot_times/h).astype(int) # converts time in seconds to correct step
    plt.figure(figsize=(20, 10))
    for p, plottime in enumerate(plot_times):
        plt.subplot(2,2,p + 1)
        plt.scatter(X[0,t[p]],X[1,t[p]], s=2)
        plt.xlim(0,25)
        plt.ylim(-5, 5)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title(f'{plottime} s')
    plt.show()



def concentration(x0, u, h, plot_times, D, N):
    '''
    x0 - starting position 
    u  - velocity field
    h  - time step
    T_sec - array of (up to) four times to show in plot
    D  - diffusion coefficient
    N  - number of particles
    '''
    X = Euler_Maruyama(x0, u, h, max(plot_times), D, N)
    nx, ny = 201, 101 # size of grid
    e = 0.1 # epsilon for Dirac delta approximation
    _, axes = plt.subplots(2, 2, figsize=(20,10))
    for i, _ in enumerate(plot_times): 
        t = int(plot_times[i]/h)
        x_span = np.linspace(0, 25, nx)
        y_span = np.linspace(-5, 5, ny)
        x_grid, y_grid = np.meshgrid(x_span, y_span) # generates gridpoints
        C = np.zeros_like(x_grid)
        for p in range(N):
            xp, yp = X[0, t, p], X[1, t, p]
            d = (x_grid - xp)**2 + (y_grid - yp)**2 # Dirac delta approximation
            C += 1/(2*np.pi*e**2)*np.exp(-d/(2*e**2)) # Adds particles to grid
        C /= N
        plt.subplot(2,2,i + 1)
        plt.title(f'{plot_times[i]} s')
        plt.contourf(x_grid, y_grid, C, cmap='Reds')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
    plt.colorbar(ax = axes.ravel().tolist())
    plt.show()
    return x_grid, y_grid, C



def source_simulation(x0, u, h, T_sec, D, Q, plot_times):
    '''
    x0 - starting position 
    u  - velocity field
    h  - time step
    T  - simulation time
    D  - diffusion coefficient
    Q  - particles released per second
    plot_times - array of (up to) four times to show in plot
    '''

    t = int(T_sec/h) # total time steps
    n_particles = int(Q*h) # new particles added every time step
    X_tot = np.zeros([2, int(T_sec/h)+1, 0])
    u = np.swapaxes(np.tile(u, (n_particles, 1)), axis1=1, axis2=0) # generates array of stacked u-vectors
    for timestep in range(t):
        X_temp = np.zeros([2, timestep, n_particles]) # array with leading zeroes for not released particles
        X_N = np.zeros([2, 1, n_particles]) # array containing the position of all particles at every time step
        n_step = 0
        X = x0
        '''
        same main simulation steps as in the first simulation, but with fewer steps for later particles and leading zeros added
        '''
        while (n_step + timestep) * h < T_sec:
            Z = np.random.normal(0, 1, (2, n_particles)) # random number for diffusion
            new_X = X_N[:,n_step,:] + u*h + np.sqrt(2*D*h)*Z # simulation of movement
            new_X = np.expand_dims(new_X, 1) # adds dimension for stacking arrays
            X_N = np.hstack((X_N, new_X)) # appends new position to total matrix
            n_step += 1 # increments step counter
        X_temp = np.concatenate((X_temp, X_N), axis = 1)  # adds particles to leading zeroes
        X_tot = np.concatenate((X_tot, X_temp), axis = 2) # adds particles to total array with all particles
    X = X_tot # name change for plots

    '''plotting'''
    N = n_particles * t # total amount of particles
    nx, ny = 201, 101 # size of grid
    e = 0.1 # epsilon for Dirac delta approximation
    _, axes = plt.subplots(2, 2, figsize=(20,10))
    for i, _ in enumerate(plot_times): 
        t = int(plot_times[i]/h) # time step of current time to plot
        x_span = np.linspace(0, 25, nx)
        y_span = np.linspace(-5, 5, ny)
        x_grid, y_grid = np.meshgrid(x_span, y_span) # generates gridpoints
        C = np.zeros_like(x_grid)
        for p in range(int(N*plot_times[i]/T_sec)): # removes not yet existing particles by only incrementing over indexes with active particles
            xp, yp = X[0, t, p], X[1, t, p]
            d = (x_grid - xp)**2 + (y_grid - yp)**2 # Dirac delta approximation
            C += 1/(2*np.pi*e**2)*np.exp(-d/(2*e**2)) # Adds particles to grid
        C /= N
        plt.subplot(2,2,i + 1)
        plt.title(f'{plot_times[i]} s')
        plt.contourf(x_grid, y_grid, C, cmap='Reds')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
    plt.colorbar(ax = axes.ravel().tolist())
    plt.show()

    '''same plotting as in particle_cloud'''
    t = (plot_times/h).astype(int)
    plt.figure(figsize=(20, 10))
    for p, plottime in enumerate(plot_times):
        plt.subplot(2,2,p + 1)
        plt.scatter(X[0,t[p]],X[1,t[p]], s=2)
        plt.xlim(0,25)
        plt.ylim(-5, 5)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title(f'{plottime} s')
    plt.show()
    return X



'''Simulation parameters'''
x0 = np.zeros([2,1])
u = np.array([0.3,0])
h = 0.1
T_sec = 60
D = 0.02
N = 1000
Q = 100
plot_times = np.array([15, 30, 45, 60])

'''Functions calls'''
# X = Euler_Maruyama(x0, u, h, T_sec, D, N)
particle_cloud(x0, u, h, plot_times, D, N)
concentration(x0, u, h, plot_times, D, N)
source_simulation(x0, u, h, T_sec, D, Q, plot_times)