import matplotlib.pyplot as plt
import numpy as np
from scipy import sin, exp, optimize


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


x = np.arange(-1.0, 50.0, 0.1)

plt.plot(x, f(x))
plt.show()

result1 = optimize.differential_evolution(f, [(1, 30)])

print(result1)

with open('pa2.txt', 'w') as f:
    f.write(str(result1['fun'][0]))

