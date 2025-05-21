import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. Загрузка данных без заголовка
data = np.loadtxt('data.csv', delimiter=',')
x = data[:, 0]
y = data[:, 1]
n = len(x)

# 2. Средние и стандартные отклонения
mx = np.mean(x)
my = np.mean(y)
sx = np.std(x, ddof=1)
sy = np.std(y, ddof=1)

# 3. Коэффициент корреляции (numpy)
r_matrix = np.corrcoef(x, y)
r = r_matrix[0, 1]

# 4. Коэффициент корреляции вручную (r2)
r2 = np.sum((x - mx) * (y - my)) / (n * sx * sy)

# 5. Линия регрессии y на x
yr = my + r * sy / sx * (x - mx)

# 6. Построение точек и линия регрессии
colors = np.abs(y - yr)

plt.scatter(x, y, c=colors, cmap='viridis', label='Исходные точки')
plt.plot(x, yr, color='red', label='Линия регрессии $y_r$', linewidth=2)

# 7. Символьная регрессия через МНК
a, b = sp.symbols('a b')
Phi = sum((y_i - a * x_i - b)**2 for x_i, y_i in zip(x, y))

# 8. Решение системы уравнений
dPhi_da = sp.diff(Phi, a)
dPhi_db = sp.diff(Phi, b)
solution = sp.solve([dPhi_da, dPhi_db], (a, b))
a_val = float(solution[a])
b_val = float(solution[b])

# 9. r3 = a * sx / sy
r3 = a_val * sx / sy

# 10. Построение прямой y = ax + b
y_line = a_val * x + b_val
plt.plot(x, y_line, color='green', linestyle='--', label='Прямая $y = ax + b$', linewidth=2)

# Оформление графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('Линейная регрессия и корреляция')
plt.colorbar(label='|y - y_r|')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Вывод результатов
print(f"mx = {mx:.4f}, my = {my:.4f}")
print(f"sx = {sx:.4f}, sy = {sy:.4f}")
print(f"Коэффициент корреляции (numpy): r = {r:.4f}")
print(f"Коэффициент корреляции (ручной): r2 = {r2:.4f}")
print(f"Параметры прямой: a = {a_val:.4f}, b = {b_val:.4f}")
print(f"Коэффициент корреляции через регрессию: r3 = {r3:.4f}")
