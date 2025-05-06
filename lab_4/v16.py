import numpy as np

n = 5
i = np.arange(1, n + 1).reshape((n, 1))
j = np.arange(1, n + 1)

H = 1.0 / (i + j - 1)

print(H)
