from ej4 import rsteffensen
from ej1 import serie_seno

xAprox_6, _ = rsteffensen(serie_seno,6,1e-5,100)
print(xAprox_6)

xAprox_3, _ = rsteffensen(serie_seno,3,1e-5,160)
print(xAprox_3)

'''
Para la aproximacion con el punto inicial 6 se requieren 69 iteraciones
Para la aproximacion con el punto inicial 3 se requiere 1 iteracion
'''
xAprox, _ = rsteffensen(serie_seno,4.5,1e-5,100)
print(xAprox)

'''
Para el caso de x0 = 4.5 el programa no para por encontrar una aproximacion con 
un erro absoluto menor a 1e-5, si no por llegar a las 100 iteraciones, se llega a un valor poco util
'''
