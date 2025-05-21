# 1
def find_elements_by_index(values, indices):

    result = []
    try:
        for index in indices:
            if not isinstance(index, int):
                raise TypeError(f"Индекс должен быть целым числом, получен {type(index)}")
                
            result.append(values[index])
        return result
    except IndexError as e:
        return f"Ошибка: индекс {index} выходит за границы списка (длина: {len(values)})"
    except TypeError as e:
        return f"Ошибка типа: {e}"



if __name__ == "__main__":
    test_values = [10, 20, 30, 40, 50]
    test_indices = [1, 3, 4]
    invalid_indices = [1, 3, 5]
    wrong_type_indices = [1, 3, "2"]
    
    print("Тест 1 (корректные индексы):")
    print(find_elements_by_index(test_values, test_indices))
    
    print("\nТест 2 (некорректный индекс):")
    print(find_elements_by_index(test_values, invalid_indices))
    
    print("\nТест 3 (неправильный тип индекса):")
    print(find_elements_by_index(test_values, wrong_type_indices))
    
    print("\nТест 4 (пустые списки):")
    print(find_elements_by_index([], [0]))


# 2
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
print(circle.radius)
print(circle.diameter)
print(circle.area()) 


# 3
class Employee:
    def __init__(self):
        self._employees = []

    def add_employee(self, name, salary):
        self._employees.append({"name": name, "salary": salary})

    @property
    def average_salary(self):
        if not self._employees:
            return 0
        total_salary = sum(emp["salary"] for emp in self._employees)
        return total_salary / len(self._employees)

    def get_sorted_employees(self):
        return sorted(self._employees, key=lambda emp: emp["salary"])

company = Employee()
company.add_employee("Алексей", 50000)
company.add_employee("Мария", 60000)
company.add_employee("Иван", 45000)

print("Средняя зарплата:", company.average_salary)
sorted_employees = company.get_sorted_employees()
for emp in sorted_employees:
    print(f"{emp['name']}: {emp['salary']}")
