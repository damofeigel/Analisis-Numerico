import numpy as np
from ej1 import serie_seno  #Aproximación de sen(x) del ejercicio 1

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

hx_pi, hf_pi = rbisec(serie_seno,[3.14,3.2],1e-5,100)      #Se aproxima a pi
print(hx_pi)                                              #Imprime historial de aproximaciones
print(hf_pi)                                              #Imprime historial de los valores funcionales    

hx_2pi, hf_2pi = rbisec(serie_seno,[6.2,6.4],1e-5,100)    #Con 5 terminos de la serie no basta para aproximar una raiz aqui
print(hx_2pi)
print(hf_2pi)

'''
INSTRUCCIONES:
Al ejecutar el programa se imprimiran por pantalla tanto las aproximaciones de las raices como su valor funcional
en el caso de la raiz 2*pi en la aproximacion no existe una raiz, por lo tanto se devuelven listas vacias

'''