import numpy as np
import matplotlib.pyplot as plt
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

X = Euler_Maruyama(np.zeros([2,1]), np.array([0,0]), 0.1, 10, 0.1, 100)
plt.plot(X[0,:], X[1,:])
plt.show()