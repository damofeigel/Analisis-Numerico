#EJ1
import matplotlib.pyplot as plt

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
'''    
def fun(x): return x**(-1)

x = [((24/25) + i/25) for i in range(1,101)]
y = [fun(i) for i in x]
hf = inewton([1,2,3,4,5],[1,1/2,1/3,1/4,1/5],x)

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
def fun(x): return 1/(1 + 25*x**2)

















