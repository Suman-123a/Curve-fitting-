#y=ae^bx curve fitting
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,4,5,7,9,12,14,17,19,21,26,30])
Y=np.array([10,11,12,13,14,16,20,21,25,28,32,43,54])
y=np.log(Y)
n=len(x)
sx2=np.sum(x**2)
sx=np.sum(x)
sy=np.sum(y)
sxy=np.dot(x,y)
A=np.array([[n,sx],[sx,sx2]])
B=np.array([sy,sxy])
c,m=np.linalg.solve(A,B)
a=np.exp(c)
yy=[]
for i in range(n):
	yi=a*np.exp(m*x[i])
	yy.append(yi)

plt.plot(x,Y,"o",label="experimental data")
plt.plot(x,yy,label="fitting curve")
plt.legend()
plt.show()



