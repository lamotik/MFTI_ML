import matplotlib.pyplot as plt
import numpy as np
from scipy import sin, exp, optimize


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


def h(x):
    return f(x).astype(int)


x = np.arange(-1.0, 50.0)

plt.plot(x, h(x))
plt.show()

result1 = optimize.minimize(h, 30, method='BFGS')
print(result1)

result2 = optimize.differential_evolution(h, [(1, 30)])
print(result2)

with open('pa3.txt', 'w') as f:
    f.write(str(result1['fun'][0]) + ' ' + str(result2['fun']))