import math
import matplotlib.pyplot as plt
import numpy as np


class Derivative:
    def __init__(self, h=1e-5):
        self.h = h

    def __get__(self, obj, objtype=None):
        """Дескриптор для доступа к производной"""
        if obj is None:
            return self
        return lambda x: (obj(x + self.h) - obj(x - self.h)) / (2 * self.h)


class ExponentialFunction:
    def __init__(self, a=1):
        self.a = a

    @property
    def derivative(self):
        """Свойство для вычисления производной"""
        h = 1e-5
        return lambda x: (self(x + h) - self(x - h)) / (2 * h)

    def __call__(self, x):
        """Вычисление значения функции в точке x"""
        return self.a * math.exp(x)

    def plot(self, x_min=-2, x_max=2, num_points=1000):
        """Построение графиков функции и её производной"""
        x = np.linspace(x_min, x_max, num_points)
        y = np.vectorize(self)(x)
        y_prime = np.vectorize(self.derivative)(x)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f"f(x) = {self.a}·eˣ", linewidth=2)
        plt.plot(x, y_prime, '--', label=f"f'(x) = {self.a}·eˣ", linewidth=2)

        plt.title(f"Экспоненциальная функция и её производная (a = {self.a})")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    exp_func = ExponentialFunction(a=2)

    print(f"f(0) = {exp_func(0)}")
    print(f"f'(0) = {exp_func.derivative(0)}")
    print(f"f(1) = {exp_func(1):.4f}")
    print(f"f'(1) = {exp_func.derivative(1):.4f}")

    exp_func.plot()
