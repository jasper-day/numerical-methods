"""
exam: 2021-2022
question: 1
"""

import numpy as np
import matplotlib.pyplot as plt

c_m = 12 # c/m, s^-1
s_m = 1500 # s/m, s^-2

polynomial = [1, 2*c_m, 3*s_m, c_m*s_m, s_m**2]

print(np.roots(polynomial))

# operating principle of the above code:
# 

# first plot the function to see what we're dealing with 

plt.title('Frequency vs characteristic polynomial')
plt.xlabel('$\\omega$')
plt.ylabel('$f(\\omega)$')
plt.axhline(0, color="black")
plt.savefig('omegas-vs-t.png')
