import numpy as np

n = 5
A = np.random.randint(0, 101, size=(n, n))
m = A.mean()

mask = (A > m / 2) & (A < 3 * m / 2)
A[mask] = 0

print(A)
