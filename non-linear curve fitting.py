#non-linear curve fitting
import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,0.5,1,1.5,2,2.5])
y=np.array([0.0674,-0.9156,1.6253,3.0377,3.3535,7.9409])
n=len(x)
sx2=np.sum(x**2)
sx=np.sum(x)
sx3=np.sum(x**3)
sx4=np.sum(x**4)
sy=np.sum(y)
sxy=np.dot(x,y)
sx2y=np.dot(x**2,y)
A=np.array([[n,sx,sx2],[sx,sx2,sx3],[sx2,sx3,sx4]])
B=np.array([sy,sxy,sx2y])
a,b,c=np.linalg.solve(A,B)
yy=[]
for i in range(n):
	yi=a+b*x[i]+c*(x**2)[i]
	yy.append(yi)
plt.title("non-linear fitting")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,"o",label="experimental data")
plt.plot(x,yy,label="fitting curve")
plt.legend()
plt.show()

