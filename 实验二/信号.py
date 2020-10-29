import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-5.0 * np.pi,5.0*np.pi,1000)  
x = np.arange(-2*np.pi,2*np.pi,0.001)
y = np.sin(x)
plt.plot(x,y,color='blue')  
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title(u'正弦信号') 
plt.show()               






