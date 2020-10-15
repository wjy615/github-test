from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
z = np.cos(x)
plt.plot(x,z)
plt.show()