import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sc

# Instrucciones
#   Al ejecutar el archivo apareceran 3 graficos
#   El primero corresponde al ej1a.
#   Los otros dos son las interpolaciones que corresponden al ej1b 


datos = np.genfromtxt("irma.csv", delimiter=",")
horas = datos[:,0]
long = datos[:,1]
lat = datos[:,2]

# Ej1a)
plt.plot(lat, long,"o")
plt.title("Puntos discretos")
#plt.show()

# Ej1b)
# p corresponde a la cordenada x de los puntos dados
# y f a f(x)

def int_lagrange(p, f):

    length = len(f)
    #Calculamos el polimonio de la lagrange para un i dado
    def li(i, x):  
        l = 1
        for j in range(0, length):
            if (j != i):
                
                l = l * (x-p[j])/(p[i]-p[j])

        return l

    def sumatoria(x):  
        # Debemos sumar f_i*li(x) para i = 0,..,length
        sum = 0
        for i in range(0, length):
            sum = sum + f[i]*li(i, x)
        return sum
    #Devuelve el polinomio
    return sumatoria

# Completamos con las horas restantes
'''
horas_restantes = []
for i in range(1,24):  # por lo que veo en csv las horas van de 1 a 24
    if i not in horas:
        horas_restantes.append(i)
horas_restantes = np.array(horas_restantes)
'''
horas_restantes = np.array([i for i in range(1,24) if i not in horas])

# Creamos los polinomios interpolantes para la longitud

lag_long = int_lagrange(horas, long)
spl_long = sc.interp1d(horas, long)

# Para la latitud
lag_lat = int_lagrange(horas, lat)
spl_lat = sc.interp1d(horas, lat)

# Grafico
fig, ax = plt.subplots()
plt.title("Interpolaciones para la longitud")
ax.plot(horas, long, "x", label = "Longitud")
ax.plot(horas_restantes, lag_long(horas_restantes), "o", label="Splines long")
ax.plot(horas_restantes, spl_long(horas_restantes), "o", label="Lagrange long")

ax.legend()

fig, ax = plt.subplots()
plt.title("Interpolaciones para la latitud")
ax.plot(horas, lat, "x", label="Latitud")
ax.plot(horas_restantes, lag_lat(horas_restantes), "o", label="Splines lat")
ax.plot(horas_restantes, spl_lat(horas_restantes), "o", label="Lagrange lat")
ax.legend()

plt.show()
