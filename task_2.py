import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
n = 10000  

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

points_below = sum(y_random <= f(x_random))
integral_area = points_below / n * (b - a) * f(b)

print(f"Значення інтеграла методом Монте-Карло: {integral_area}")

fig, ax = plt.subplots()

x = np.linspace(-0.5, 2.5, 400)
y = f(x)
ax.plot(x, y, 'r', linewidth=2)

ax.scatter(x_random, y_random, color='blue', s=1)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Метод Монте-Карло для обчислення інтеграла f(x) = x^2')
plt.grid()
plt.show()


# Обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)

# Виведення результату
print("Значення інтеграла за допомогою scipy:", result)