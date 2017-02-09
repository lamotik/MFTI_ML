from nltk.app.chartparser_app import app
from scipy import linalg, sin, exp
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


def approx_f(x, coefs):
    size = np.size(coefs, 0)
    result = np.zeros(np.size(x, 0))
    for k, v in np.ndenumerate(x):
        result[k[0]] = np.sum(np.power(np.repeat(v, size), np.arange(size)).dot(coefs))
    return result


x = np.arange(16, 0.5)

A1 = np.array([[1, 1], [1, 15]])
b1 = np.array([f(1), f(15)])
x1 = linalg.solve(A1, b1)
print(x1)

plt.plot(x, approx_f(x, x1))
plt.show()


A2 = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 225]])
b2 = np.array([f(1), f(8), f(15)])
x2 = linalg.solve(A2, b2)
print(x2)

plt.plot(x, approx_f(x, x2))
plt.show()

A3 = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b3 = np.array([f(1), f(4), f(10), f(15)])
x3 = linalg.solve(A3, b3)
print(x3)

plt.plot(x, approx_f(x, x3))
plt.show()
