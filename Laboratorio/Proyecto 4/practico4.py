import matplotlib.pyplot as plt
import numpy as np
import math

datos = np.loadtxt('datos1a.dat')

x = datos[:,0]
y = datos[:,1]

n = len(x)

'''
sum_xi = sum(x)
sum_yi = sum(y)
sum_xi2 = sum(x**2)
sum_xi_yi = sum(x*y)
#sum_yi2 = sum(y**2)

d = (n*sum_xi2 - sum_xi **2)
b = (sum_xi2 * sum_yi - sum_xi_yi * sum_xi)/d

m = (n* sum_xi_yi - sum_xi * sum_yi)/d

def fun(x): return m*x + b

gr = np.linspace(0,7,2)
fgr = fun(gr)

pl.plot(x,y,'o')
pl.plot(gr,fgr)
pl.show()
'''

'''
array_1 = np.ones(n)

sum_xi = np.dot(x,array_1)
sum_yi = np.dot(y,array_1)
sum_xi2 = np.dot(x*x, array_1)
sum_xi_yi = np.dot(x*y, array_1)

d = (n*sum_xi2 - sum_xi **2)
b = (sum_xi2 * sum_yi - sum_xi_yi * sum_xi)/d

m = (n* sum_xi_yi - sum_xi * sum_yi)/d

def fun(x): return m*x + b

gr = np.linspace(0,7,2)
fgr = fun(gr)

pl.plot(x,y,'o')
pl.plot(gr,fgr)
pl.show()

'''
'''
def recta(x): return 3/4*x - 1/2

x = np.linspace(0,10,20)
y = recta(x)

v = np.random.randn(20) 
v0 = recta(x) + v 

f = np.polyfit(x,v0,1)



plt.plot(x,y)
plt.plot(x,np.polyval(f,x))
plt.show()

'''
def arcsen(x): return [math.asin(i) for i in x]

def cos(x): return [math.cos(i) for i in x] 


x = np.linspace(0,1,50)
#x = [np.random.uniform(0,1) for i in range(50)]
y = arcsen(x)

arr = np.ones((50,2), dtype=np.float32)

for i in range(50):
	arr[i][0] = arr[i][0] * x[i]
	

arr2 = arr.transpose((1,0))

# At Ax = At B

print(arr)
print(arr2)

aasdas = arr2 * arr
print(aasdas)























