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

''' 
INSTRUCCIONES: 
Probar la función para aproximación 
para determinar la raiz de cualquier funcion
elegir un x0 cercano

'''
