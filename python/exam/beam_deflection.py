import numpy as np
import matplotlib.pyplot as plt

def y(x):
    L = 800 # cm
    E = 4e4 # kN/cm^2
    I = 4e4 # cm^4
    w_0 = 3.5 # kN/cm
    y = w_0/(120 * E * I * L) * (-x**5 + 2*L**2*x**3 - L**4 * x)
    return y

xs = np.linspace(0,800,1000)
ys = y(xs)
min_ind = np.argwhere(ys - min(ys) == 0)

#def minimize_fn 

plt.plot(xs,y(xs))
# minimum point
plt.scatter(xs[min_ind], ys[min_ind], color="red")
plt.text(xs[min_ind], ys[min_ind], f"({xs[min_ind]}, {ys[min_ind]})")
plt.title("X position vs deflection")
plt.ylabel("Deflection [cm]")
plt.xlabel("X position [cm]")
plt.savefig('deflection.png')
