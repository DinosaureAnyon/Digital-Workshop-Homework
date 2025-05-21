import math


class Shape:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределен в подклассе")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть переопределен в подклассе")


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    try:
        circle = Circle(5)
        print("Circle area:", circle.area())
        print("Circle perimeter:", circle.perimeter())

        rectangle = Rectangle(4, 6)
        print("Rectangle area:", rectangle.area())
        print("Rectangle perimeter:", rectangle.perimeter())

    except ValueError as e:
        print("Ошибка:", e)
    except NotImplementedError as e:
        print("Ошибка:", e)
