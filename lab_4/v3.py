import numpy as np

n = 5  # можно изменить
A = np.random.randint(0, 101, size=(n, n))
m = A.mean()

# Условие: элементы больше m/2 и меньше 3m/2
mask = (A > m / 2) & (A < 3 * m / 2)
A[mask] = 0

print(A)
