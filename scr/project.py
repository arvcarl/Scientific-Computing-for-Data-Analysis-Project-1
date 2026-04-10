import numpy as np
import matplotlib.pyplot as plt
import time

'''from pathlib import Path

this_dir = Path(__file__).resolve().parent
sat_path = this_dir / "placeholder" '''

def Euler_Maruyama(x0, u, h, T, D, N):
    '''
    x0 - starting position 
    u  - velocity field
    h  - time step
    T  - simulation time
    D  - diffusion coefficient
    N  - number of particles
    '''
    X_N = np.zeros([2, int(T/h)+1, 0]) # array for position over time of every particle
    for p in range(N):
        X = x0
        n_step = 0 # number of steps
        while n_step*h < T: 
            Z = np.random.normal(0, 1, 2)
            new_X = X[:,-1] + u*h + np.sqrt(2*D*h)*Z # calculates position of next step
            X = np.column_stack((X, new_X)) # appends next step to X
            n_step += 1
        X_N = np.dstack((X_N, X)) # appends particle X_p to array 
    return X_N
'''
X_N is a three dimensional array
1: Spacial dimensions (in this case 2)
2: Time steps
3: Particle number
'''


def particle_cloud(x0, u, h, T_sec, D, N):
    X = Euler_Maruyama(x0, u, h, max(T_sec), D, N) # runs simulation 
    t = (T_sec/h).astype(int) # converts time in seconds to correct step

    plt.subplot(2,2,1)
    plt.scatter(X[0,t[0]],X[1,t[0]])
    plt.xlim(0,25)
    plt.ylim(-5, 5)
    plt.title('15 s')

    plt.subplot(2,2,2)
    plt.scatter(X[0,t[1]],X[1,t[1]])
    plt.xlim(0,25)
    plt.ylim(-5, 5)
    plt.title('30 s')

    plt.subplot(2,2,3)
    plt.scatter(X[0,t[2]],X[1,t[2]])
    plt.xlim(0,25)
    plt.ylim(-5, 5)
    plt.title('45 s')

    plt.subplot(2,2,4)
    plt.scatter(X[0,t[3]],X[1,t[3]])
    plt.xlim(0,25)
    plt.ylim(-5, 5)
    plt.title('60 s')

    plt.show()

h = 0.1
u = np.array([0.3,0])


#X = Euler_Maruyama(np.zeros([2,1]), np.array([0.3,0]), h, 60, 0.02, 200)
#plt.plot(X[0,:], X[1,:])
#plt.show()
#T_sec = np.array([15, 30, 45, 60])
#particle_cloud(np.zeros([2, 1]), np.array([0.3, 0]), 0.1, T_sec, 0.02, 100)


def concentration(x0, u, h, T_sec, D, N):
    X = Euler_Maruyama(x0, u, h, max(T_sec), D, N)
    nx, ny = 201, 101 # size of grid
    e = 0.1 # epsilon for Dirac delta approximation
    _, axes = plt.subplots(2, 2)
    for i, _ in enumerate(T_sec): 
        t = int(T_sec[i]/h)
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
        plt.title(f'{T_sec[i]} s')
        plt.contourf(x_grid, y_grid, C)
    plt.colorbar(ax = axes.ravel().tolist())
    plt.show()
    return x_grid, y_grid, C

def source_simulation(x0, u, h, T_sec, D, Q):
    t = int(T_sec/h) # total time steps
    n_particles = int(Q*h) # new particles added every time step
    X_tot = np.zeros([2, int(T_sec/h)+1, 0])
    for timestep in range(t):
        print(timestep)
        X_temp = np.zeros([2, timestep, n_particles])
        X_N = np.zeros([2, int(T_sec/h)+1 - timestep, 0]) # array for position over time of every particle
        for p in range(n_particles):
            X = x0
            n_step = 0 # number of steps
            while (n_step + timestep) *h < T_sec: 
                Z = np.random.normal(0, 1, 2)
                new_X = X[:,-1] + u*h + np.sqrt(2*D*h)*Z # calculates position of next step
                X = np.column_stack((X, new_X)) # appends next step to X
                n_step += 1
            X_N = np.dstack((X_N, X)) # appends particle X_p to array 
        X_temp = np.concatenate((X_temp, X_N), axis = 1)
        X_tot = np.concatenate((X_tot, X_temp), axis = 2)
    
    return X_tot


X = source_simulation(np.zeros([2,1]), np.array([0.3,0]), h, 60, 0.02, 100)

'''

T_sec = np.array([15, 30, 45, 60])
t = (T_sec/h).astype(int)

plt.subplot(2,2,1)
plt.scatter(X[0,t[0]],X[1,t[0]])
plt.xlim(0,25)
plt.ylim(-5, 5)
plt.title('15 s')

plt.subplot(2,2,2)
plt.scatter(X[0,t[1]],X[1,t[1]])
plt.xlim(0,25)
plt.ylim(-5, 5)
plt.title('30 s')

plt.subplot(2,2,3)
plt.scatter(X[0,t[2]],X[1,t[2]])
plt.xlim(0,25)
plt.ylim(-5, 5)
plt.title('45 s')

plt.subplot(2,2,4)
plt.scatter(X[0,t[3]],X[1,t[3]])
plt.xlim(0,25)
plt.ylim(-5, 5)
plt.title('60 s')

plt.show()
'''
