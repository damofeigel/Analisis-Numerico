from tkinter.messagebox import NO
import numpy as np


def intenumcomp(func, a, b, N, regla):
        if regla == "trapecio":
            return trapecio(func,a,b,N)
        elif regla == "punto medio":
            return punto_medio(func,a,b,N)  
        if regla == "Simpson":
            return simpson(func,a,b,N)
        else:
            print("NOO CUALQUIER COSA PUSISTE") 
            return None

def simpson(fun, a,b,N):
    if N%2 != 0:
        print("N debe ser par")
        return None
    h = (b-a)/(2*N)
    sx0 = fun(a) + fun(b)
    sx1 = 0   #Suma impares
    sx2 = 0   #Suma pares
    x = a
    for i in range(1,2*N):
        x += h
        if i%2 == 0:
            sx2 += fun(x)
        else:
            sx1 += fun(x)
    sx = (sx0 + 2*sx2 + 4*sx1)*(h/3)
    return sx

def fun(x): return x**3
print(intenumcomp(fun,0,1,4,"Simpson"))
def trapecio(fun, a, b, N):
    x = a
    sum = 0
    h = (b-a)/N
    for i in range(1, N):
        sum += fun(a + i*h)
    return (h/2)*(fun(a) + fun(b) + 2*sum)
#print(intenumcomp(fun,0,1,10000000,"trapecio"))
def punto_medio(fun, a, b, N):
    h = (b-a)/(N+2)
    sum = 0
    x = a
    for j in range(-1,N+2):
        if j%2== 0:
            sum += fun(a + (j+1)*h)
    return (2*h)*(sum)
#print(intenumcomp(fun,0,1,1000000,"punto medio"))
