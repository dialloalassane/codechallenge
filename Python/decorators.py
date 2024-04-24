import numpy as np 


def wrapper(f,x, N):
    def monteCarlo(g):  
        return np.sum([g(x[i] for i in range(N)])
    return monteCarlo(f)


@wrapper 
