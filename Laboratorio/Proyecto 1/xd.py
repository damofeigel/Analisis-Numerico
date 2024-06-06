from cmath import sqrt
import math
import random
def overflow(x):
    while not math.isinf(x):
        x=x**2
        print(x)

def underflow(x):
    while x != 0:
        x = x/2
        print(x)

def wow():
    y = 0
    while y < 10:
        y = y + 0.1
        print(y)

def fact(n):
    if n == 0:
        n = 1
    else:
        n = n * (fact(n-1))    
    print(n)
    return n 
         
def mayor(x,y):
    if x > y:
        print(f"{x} es mayor que {y}")
    elif x==y:
        print("son iguales")    
    elif x < y:
        print(f"{y} es mayor que {x}")    

def potencias(x,n):
    if n == 0:
        x = 1
    else:
        x = x*potencias(x,n-1)

    print(x)    
    return x

def bashkara(a,b,c):

    if b ** 2 - 4 * a * c < 0 :
        print("NO SOLUCION FLACO")
    elif b ** 2 - 4 * a * c == 0 :
        n = (-b + (b**2 - 4 * a * c)** (1/2))/(2*a)
        print(f"{n} Unica solucion real")
        return n
    elif b ** 2 - 4 * a * c > 0 :  
        n = (-b + (b**2 - 4 * a * c)** (1/2))/(2*a)
        m = (-b - (b**2 - 4 * a * c)** (1/2))/(2*a)
        print(f"{n},{m} son las soluciones reales")
        return n,m

def horn(coef, x):
    res = coef[0]
    for i in range(1,len(coef)):
        res = coef[i] + x * res
    return res    

p = horn([1,-5,6,2],5)
print(p)

def son_reciprocos(n,m):
    if n*m == 1:
        return True
    else:
        return False
""""
for _ in range(100):
    x = 1 + random.random()
    y = 1/x
    if not son_reciprocos(x,y):
        print(x)
"""
def f(x):
    res = (x**2+1)**(1/2) - 1
    return res
def g(x):
    res = x**2/((x**2+1)**(1/2)+1)    
    return res  
""""
for _ in range(20):
    x = 8**-_
    print(f"f(x)={f(x)}, g(x)={g(x)}")
""" 
def son_ortogonales([x1,y1],[]):
    if ((x1*y1 + x2*y2) == 0):
        return True
    else:
        return False
son_ortogonales((1,2),(2,1))


