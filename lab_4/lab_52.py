# Задание 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

N = 10000
n = 50
a, b = 0, 1  

X = np.random.uniform(a, b, size=(N, n))

Sn = np.sum(X, axis=1)

A = (a + b) / 2
D = ((b - a) ** 2) / 12
An = n * A
Dn = n * D

X_norm = (Sn - An) / np.sqrt(Dn)

plt.hist(X_norm, bins=50, density=True, alpha=0.6, color='b', label='Гистограмма')

x = np.linspace(-4, 4, 400)
plt.plot(x, norm.pdf(x), 'r-', label='Стандартное нормальное распределение')

plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.title('Центральная предельная теорема')
plt.legend()
plt.grid(True)
plt.show()
