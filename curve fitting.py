#curve fitting
import numpy as np
import matplotlib.pyplot as plt
#log(T)
x=np.array([2.90,3,3.04,3.09,3.11,3.14,3.18,3.19,3.23,3.24,3.25,3.26,3.27,3.28,3.30,3.33,3.37])
#log(P)
y=np.array([2.18,2.50,2.66,2.86,2.98,3.09,3.21,3.26,3.39,3.43,3.50,3.61,3.69,3.71,3.78,3.90,3.97])
n=len(x)
sx2=np.sum(x**2)
sx=np.sum(x)
sy=np.sum(y)
sxy=np.dot(x,y)
xm=np.mean(x)
ym=np.mean(y)
m=(sxy-n*xm*ym)/(sx2-n*xm**2)
c=(sy-m*sx)/n
yy=[]
for i in range(n):
	yi=m*x[i]+c
	yy.append(yi)
plt.title("Stepan's Law Verification (The Graph of Log T vs Log P)")
plt.xlabel("Log T----------->")
plt.ylabel("Log P----------->")
plt.plot(x,y,"o",label="experimental data")
plt.plot(x,yy,label="fitting curve")
plt.legend()
plt.show()



