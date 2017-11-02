import pandas as pd
import numpy as np
from scipy.optimize import minimize

def van(tir, cf):
    '''
    Return VAN
        tir = interest rate
        cf  = (array) cash flows
    '''

    if not isinstance(cf, np.ndarray): return('cf must be an array')

    v = 1 / (1 + tir) ** np.arange(cf.size)
    van = cf * v
    return(van.sum())

x = van(0.05, np.array([-100, 5, 5, 5, 105]))

def fitness(tir, cf):
    return(np.abs(van(tir, cf)))

fitness(0.05, np.array([-100, 5, 5, 5, 105]))

x = minimize(fitness, 0, np.array([-100, 5, 5, 5, 105]), method='BFGS')

def tir(cf):
    if not isinstance(cf, np.ndarray): return('cf must be an array')

    fit = lambda tir, cf: np.abs(van(tir, cf))

    tir = minimize(fit, 0, np.array([-100, 5, 5, 5, 105]), method='BFGS')

    return(x.x)
