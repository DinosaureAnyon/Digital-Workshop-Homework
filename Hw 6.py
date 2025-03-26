import math
import matplotlib.pyplot as plt
import numpy as np


class Derivative:
    def __init__(self, h=1e-5):
        self.h = h

    def __call__(self, x):
        """Вычисление производной в точке x"""
        instance = self.instance
        return (instance(x + self.h) - instance(x - self.h)) / (2 * self.h)

    def __get__(self, instance, owner):
        """Дескриптор для доступа к производной из класса ExponentialFunction"""
        self.instance = instance
        return self


class ExponentialFunction:
    def __init__(self, a=1):
        self.a = a
        self.derivative = Derivative()

    def __call__(self, x):
        """Вычисление значения функции в точке x"""
        return self.a * math.exp(x)

    def plot(self, x_min=-2, x_max=2, num_points=1000):
        """Построение графиков функции и её производной"""
        x_vals = np.linspace(x_min, x_max, num_points)
        y_vals = [self(x) for x in x_vals]
        y_prime_vals = [self.derivative(x) for x in x_vals]

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f"f(x) = {self.a}·eˣ", linewidth=2)
        plt.plot(x_vals, y_prime_vals, label=f"f'(x) = {self.a}·eˣ", linestyle='--', linewidth=2)

        plt.title(f"График функции f(x) = {self.a}·eˣ и её производной")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    exp_func = ExponentialFunction(a=2)

    print(f"f(0) = {exp_func(0)}")  # 2.0
    print(f"f'(0) = {exp_func.derivative(0)}")  # 2.0

    print(f"f(1) = {exp_func(1)}")  # ~5.4366
    print(f"f'(1) = {exp_func.derivative(1)}")  # ~5.4366

    exp_func.plot()