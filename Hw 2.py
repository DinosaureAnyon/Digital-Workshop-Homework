# 2
class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0.0

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_salary(self) -> float:
        return self.__salary

    def set_bonus(self, bonus: float) -> None:
        self.__bonus = bonus

    def get_bonus(self) -> float:
        return self.__bonus

    def get_total_salary(self) -> float:
        return self.__salary + self.__bonus

employee = Employee("Иван Иванов", 30, 50000.0)
print(f"Имя: {employee.get_name()}")
print(f"Возраст: {employee.get_age()}")
print(f"Оклад: {employee.get_salary()}")
print(f"Бонус: {employee.get_bonus()}")
print(f"Общая зарплата: {employee.get_total_salary()}")

employee.set_bonus(10000.0)
print(f"Новый бонус: {employee.get_bonus()}")
print(f"Общая зарплата после бонуса: {employee.get_total_salary()}")

# 3
class Recipe:
    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self) -> None:
        print("Ингредиенты для рецепта:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self) -> None:
        print(f"Готовим блюдо: {self.name}")
        print("Блюдо готово! Приятного аппетита!")

recipe = Recipe("Омлет", ["Яйца", "Молоко", "Соль", "Масло"])
recipe.print_ingredients()
recipe.cook()