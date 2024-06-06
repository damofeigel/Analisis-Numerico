import numpy as np 
import matplotlib.pyplot as plt
import math

def integral_simpson(x):
    fun = lambda y : 1/y
    h = (x-1)/100
    xi = np.linspace(1, 1 + 100*h, 100+1) # xj = a + j 
    sumatoria = fun(1) + fun(x)
    for j in range(1, int(100/2)+1):
        sumatoria += 4*fun(xi[2*j - 1])
        if j != int(100/2):
            sumatoria += 2 * fun(xi[2*j])
    integral : int = sumatoria*(h/3)
    return integral





