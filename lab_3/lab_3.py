import sympy as sp

# Определяем переменную
x = sp.symbols('x')

# Определяем выражения для левого и правого предела
f_left = (sp.acot(sp.sin(x))) / (sp.sin(x**2) + 1 - sp.cos(x))
f_right = (sp.ln(1 + sp.tan(x))) / (sp.sin(sp.sqrt(x)) * sp.asin(sp.sqrt(x)))

# Вычисляем пределы при x -> 0 слева и справа
limit_left = sp.limit(f_left, x, 0, dir='-')
limit_right = sp.limit(f_right, x, 0, dir='+')

# Решаем уравнение для A
A = sp.symbols('A')
equation_A = sp.Eq(A * limit_left, limit_right)
solution_A = sp.solve(equation_A, A)

# Значение B должно быть равно пределу функции (для непрерывности)
B = sp.symbols('B')
equation_B = sp.Eq(B, limit_right)
solution_B = sp.solve(equation_B, B)

solution_A, solution_B
