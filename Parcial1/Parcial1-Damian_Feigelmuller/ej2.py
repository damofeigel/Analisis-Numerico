import math
import matplotlib.pyplot as plt
from ej1 import serie_seno      #Aproximación de sen(x) del ejercicio anterior

x = [0.01 * i for i in range(0,641)]             #Lista con valores para x
y = [math.sin(0.01*i) for i in range(0,641)]     #Lista con el valor de sen(x)
hf = [serie_seno(0.01*i) for i in range(0,641)]  #Lista con el valor de la aproximación

fig, ax = plt.subplots(figsize=(7, 5), layout='constrained')
ax.plot(x, y, label='sen(x)')  
ax.plot(x, hf, label='Serie Taylor de sen(x)') 
ax.set_xlabel('Eje x ')
ax.set_ylabel('Eje y ')    
ax.legend()
plt.show() 

'''
Instrucciones:
El grafico contiene la funcion seno(x) y su aproximación en el intervalo [0,6.4] 
El grafico aparecerá al ejecutar el codigo

'''
