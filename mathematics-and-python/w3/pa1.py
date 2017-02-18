import matplotlib.pyplot as plt
import numpy as np
from scipy import sin, exp, optimize


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


x = np.arange(-1.0, 50.0, 0.1)

plt.plot(x, f(x))
plt.show()

result1 = optimize.minimize(f, 2, method='BFGS')
result2 = optimize.minimize(f, 30, method='BFGS')

print(result1)
print(result2)

with open('pa1.txt', 'w') as f:
    f.write(str(result1['fun']) + ' ' + str(result2['fun']))
