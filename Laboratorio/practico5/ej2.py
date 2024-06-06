import numpy as np
from math import e
import ej1

fun = lambda x : x**3 #np.exp(-x)
valor_exacto = 0.25 #-np.exp(-1) + np.exp(0)

for N in [4,10,20]:
    error_simpson = np.abs(valor_exacto - ej1.intenumcomp(fun, 0, 1, N, "Simpson"))
    print(f"error simpson: {error_simpson} para {N} intervalos")
    error_trapecio = np.abs(valor_exacto - ej1.intenumcomp(fun, 0, 1, N, "trapecio"))
    print(f"error trapecio: {valor_exacto - error_trapecio} para {N} intervalos")
    error_pm = np.abs(valor_exacto - ej1.intenumcomp(fun, 0, 1, N, "punto medio"))
    print(f"error trapecio: {valor_exacto - error_pm} para {N} intervalos")


