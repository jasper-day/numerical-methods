import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1e-5,4,1000)
f = lambda x: 1/(np.sin(x)) + 1/4
plt.plot(x, [max(min(f_x, 4),-4) for f_x in f(x)])
plt.plot(x,x)
plt.savefig('graphical_iteration.png')


