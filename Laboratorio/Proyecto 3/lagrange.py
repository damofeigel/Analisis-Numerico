import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from math import cos, pi

#EJ1
def ilagrange(x,y,z):
    assert(len(x) == len(y))   
    
    hli = []

    for i in range(len(z)):    
        sum = 0
        for j in range(len(x)):
            res = 1
            for k in range(len(x)):
                if j != k:
                    res = res*((z[i]-x[k])/(x[j]-x[k]))
            sum = sum + res*y[j]
        hli.append(sum)
    return hli
print("LAGRANGE: \n")
print(ilagrange([-1.5,-0.75,0,0.75,1.5],[-14.1014,-0.931596,0,0.9313596,14.1014],[1,2,3]))

#EJ2
def horn_newton(zj,x,coefs):
	n = len(coefs)
	valor = coefs[n-1]
	for i in range(n-2,-1,-1):
		valor = coefs[i] + (zj - x[i])*valor
	return valor


def inewton(x,y,z):
    assert(len(x) == len(y))
    
    n = len(y) 
    
    c = [[0.0]*i for i in range(n,0,-1)] 
    for i in range(n):
        c[i][0] = y[i] 

    for i in range(1,n): 
    	    for j in range(n-i): 
    	        c[j][i] = (c[j+1][i-1] - c[j][i-1])/(x[j+i]-x[j])

    coef = c[0]
    w = [horn_newton(i,x,coef) for i in z]

    return w

    
def fun(x): return x**(-1)

x = [((24/25) + i/25) for i in range(1,101)]
y = [fun(i) for i in x]
hf = inewton([1,2,3,4,5],[1,1/2,1/3,1/4,1/5],x)
'''
fig, ax = plt.subplots()
ax.plot(x,y, label='1/x')
ax.plot(x,hf, label='newton')
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y') 
for i in range(1,5): ax.plot(i,fun(i),'x')
plt.grid()
plt.legend()
plt.show()
'''
'''
print("NEWTON: \n")
print(inewton([-1.5,-0.75,0,0.75,1.5],[-14.1014,-0.931596,0,0.9313596,14.1014],[1,2,3]))
'''

'''
f = lambda x : 1 / (1 + 25*x**2)

a = -1
b = 1
h = (b-a)/199
x_plot = [-1 + h*i for i in range(200)]

f_plot = [f(x) for x in x_plot]

fig = plt.figure()
axes = []

for n in range(1,16):
	# interpolación de p
	x_inter_p = [2*(i-1)/n -1 for i in range(1,n+2)]
	f_inter_p = [f(x) for x in x_inter_p]
	p_plot = inewton(x_inter_p,f_inter_p,x_plot)
	# interpolación de q
	x_inter_q = [cos(pi*(2*i+1)/(2*n+2)) for i in range(n+1)]
	f_inter_q = [f(x) for x in x_inter_q]
	q_plot = inewton(x_inter_q,f_inter_q,x_plot)
	axes.append(fig.add_subplot(5,3,n)) # fila, columna, idx
	axes[-1].plot(x_plot, f_plot)
	axes[-1].plot(x_plot, p_plot)
	axes[-1].plot(x_plot, q_plot)
	axes[-1].grid()

plt.show()

'''
 
datos = np.loadtxt('datos_aeroCBA.dat')

year = datos[:,0]
temp = datos[:,1]

plt.plot(year,temp)
plt.show()
f = interpolate.interp1d(year, temp)

all_year = np.arange(1957,2016)  
temp = f(all_year)













    



