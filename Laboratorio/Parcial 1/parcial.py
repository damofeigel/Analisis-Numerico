import math
from math import pi
import matplotlib.pyplot as plt
import numpy as np


#EJ1
def serie_seno(x):
    res = 0
    i = 0
    while i < 100:
        res = res + (x**(2*i+1))*(((-1)**i)/math.factorial(2*i+1)) 
        i += 1
    return res

#EJ2
x = [0.01 * i for i in range(0,641)]
y = [math.sin(0.01*i) for i in range(0,641)]
hf = [serie_seno(0.01*i) for i in range(0,641)]

fig, ax = plt.subplots(figsize=(5, 3), layout='constrained')
ax.plot(x, y, label='sen(x)')  
ax.plot(x, hf, label='Serie Taylor de sen(x)') 
ax.set_xlabel('eje x ')
ax.set_ylabel('eje y ')    
ax.legend()
plt.show()

#EJ3
def rbisec(fun,I,err,mit):
    u = fun(I[0])   
    v = fun(I[1])     
    e = I[1] - I[0]
    hx = []
    hf = []
    
    
    if np.sign(v) == np.sign(u):
        
        print(f"No hay raiz en el intervalo [{I[0]},{I[1]}]")
        return hx,hf
    
    for k in range(mit):
    
        e = e/2
        c = I[0] + e
        w = fun(c)
        
        hx.append(c)
        hf.append(w)   
        
        if abs(e) < err:
            #print(f"Se satisface la tolerancia del error => f_c = {w}, c = {c}")
            break
        
        if np.sign(w) != np.sign(u):     
            I[1] = c
            v = w
    
        else:                       
            I[0] = c
            u = w
    
    return hx,hf

#EJ3
'''
hx_pi, hf_pi = rbisec(serie_seno,[3.1,3.2],1e-5,100)        #Se aproxima a pi
print(hx_pi)
hx_2pi, hf_2pi = rbisec(serie_seno,[6.2,6.4],1e-5,100)    #Con 5 terminos de la serie no basta para aproximar una raiz aqui
print(hx_2pi)
'''
#EJ4
def rsteffensen(fun,x0,err,mit):
    hx = []
    hf = []
    f = fun(x0)
    contador = 0

    for i in range(mit):    
          
        xn = x0 - (f**2)/(fun(x0 + f)-f)
        f = fun(xn)

        hx.append(xn)
        hf.append(f)

        contador += 1

        if abs(f) < err:  
            break

        x0 = xn
        
    print(f"Numero de iteraciones: {contador}")
    return hx,hf



xAprox, _ = rsteffensen(serie_seno,6,1e-5,100)
print(xAprox)
