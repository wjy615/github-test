import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
import math

x=np.arange(0.05,3,0.05)
y1=[5 for i in x]
plt.plot(x,y1,linewidth=2,label='常函数：y=5')
# w = pi/2
fs = 0.25
y5=[math.pow(2,i) for i in x]
plt.plot(x,y5,linewidth=2,label='指数函数：y=$2^x$')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('连续实指数信号')
plt.ylim(-1.0,5.0)
plt.show()