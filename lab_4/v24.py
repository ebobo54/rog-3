import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
v = np.array([3, 4])

matches = np.all(A == v, axis=1)

indices = np.where(matches)[0]

if indices.size > 0:
    print(indices[0])
else:
    print("Нет совпадений")
