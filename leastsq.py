#作业：请采用leastsq拟合一条曲线
#y=a*x*x + b*x +c
#X:  0,1,2,3,-1,-2,-3
#Y: -1.22,1.85,3.22,10.29,2.21,3.72,8.7
#name:Huang Weihao
#Date:2018/4/27

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(7,7))

x = np.linspace(-4,4,1000)
X=np.array([0,1,2,3,-1,-2,-3])
Y=np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])

def f(p):
    a, b,c = p
    return(Y-a*X*X + b*X +c)

r = leastsq(f, [1,0,0])
a,b,c = r[0]
print("a=",a,"b=",b,"c=",c)

plt.scatter(X,Y, s=50, alpha=1, marker='o',label=u'data point')

y=a*x*x + b*x +c

ax = plt.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=3, linestyle=":",markersize=10, label=u'Curve fitting')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'X')
plt.ylabel(u'Y')

plt.xlim(-x.max() * 1.1, x.max() * 1.1)
plt.ylim( Y.min()*1.5, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()