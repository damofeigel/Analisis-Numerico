from math import factorial

def serie_seno(x):
    res = 0
    i = 0
    while i < 5:
        res = res + (x**(2*i+1))*(((-1)**i)/factorial(2*i+1)) 
        i += 1
    return res

'''
INSTRUCCIONES:
Probar la aproximación con algun "x" y mostrar el resultado por pantalla

ej  aprox = serie_seno(3.1415)
    print(aprox)

'''
