import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
from pathlib import Path

this_dir = Path(__file__).resolve().parent
sat_path = this_dir / "mättnadskurva_kväve.txt"
=======
def Euler_Maruyama(x0, u, h, T, D, N):
    '''
    x0 - starting position 
    u  - velocity field
    h  - time step
    T  - simulation time
    D  - diffusion coefficient
    N  - number of particles
    '''
    X = x0
    n_step = 0 # number of steps
    while n_step*h <= T: 
        Z = np.random.normal(0, 1, 2)
        new_X = X[:,-1] + u*h + np.sqrt(2*D*h)*Z
        X = np.column_stack((X, new_X))
        n_step += 1
    return X

X = Euler_Maruyama(np.zeros([2,1]), np.array([0.0,0]), 0.1, 100, 0.2, 1)
plt.plot(X[0,:], X[1,:])
plt.show()
>>>>>>> b11f79f (Added implementation of Euler-Maruyama method)
