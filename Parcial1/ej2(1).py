import matplotlib.pyplot as plt

#  Instrucciones
#   Al ejecutar el archivo aparecerá un grafico correspondiente al ej2a
#   Y luego se imprimirá por consola el resultado de ej2b
# 

# Creamos dos listas con los puntos dados
x = [0,1.5,2,2.9,4,5.6,6,7.1,8.05,9.2,10,11.3,12]
y = [0.1,0.2,1,0.56,1.5,2.0,2.3,1.3,0.8,0.6,0.4,0.3,0.2]

# A
'''
plt.plot(x, y)
plt.show()
'''
# Graficamos
fig, ax = plt.subplots()
ax.plot(x, y, "x")

plt.show()

#B

def trapecio_adaptativo(x, y):
    if (not sorted(x)): 
        print("Deben estar ordenados")
        return None
    if (len(y) != len(x) or len(x) < 2):
        print("Las listas son de tamaño incorrecto")
        return None
    # En res voy a guardar la sumatoria de 
    # la regla en cada subintervalo
    length = len(x)
    res = 0
    for i in range(length - 1):
        res = res + (x[i+1] - x[i])/2 * (y[i] + y[i+1])
    return res


print(f"Se deben remover {10.0*trapecio_adaptativo(x,y)} m^3 de tierra")

