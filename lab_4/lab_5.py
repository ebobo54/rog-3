# Задание 1
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, 1],
              [1, 3]])

values, vectors = np.linalg.eig(A)

b1 = vectors[:, 0] / np.linalg.norm(vectors[:, 0])
b2 = vectors[:, 1] / np.linalg.norm(vectors[:, 1])

theta = np.linspace(0, 2 * np.pi, 300)
x = np.cos(theta)
y = np.sin(theta)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].plot(x, y, label='Единичная окружность')
axs[0].quiver(0, 0, b1[0], b1[1], angles='xy', scale_units='xy', scale=1, color='r', label='b1')
axs[0].quiver(0, 0, b2[0], b2[1], angles='xy', scale_units='xy', scale=1, color='g', label='b2')
axs[0].axis('equal')
axs[0].grid(True)
axs[0].legend()
axs[0].set_title('Собственные векторы')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

coords = np.vstack((x, y))
transformed = A @ coords
axs[1].plot(transformed[0], transformed[1], label='Образ окружности')
Ab1 = A @ b1
Ab2 = A @ b2
axs[1].quiver(0, 0, Ab1[0], Ab1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Ab1')
axs[1].quiver(0, 0, Ab2[0], Ab2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Ab2')
axs[1].axis('equal')
axs[1].grid(True)
axs[1].legend()
axs[1].set_title('Отображение окружности')
axs[1].set_xlabel('u')
axs[1].set_ylabel('v')

plt.tight_layout()
plt.show()
