# 3
class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def __getattr__(self, item):
        return "This attribute is not available"

c = Car("Toyota", "Corolla")
print(c.make)
print(c.model)
print(c.color)
print(c.year)

# 4
class Rectangle:
    __slots__ = ('width', 'height')

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name not in self.__slots__:
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(name, value)

r = Rectangle(10, 20)
r.width = 15  # Успешно
r.height = 25  # Успешно

try:
    r.color = 'red'
except AttributeError as e:
    print(f"AttributeError: {e}")