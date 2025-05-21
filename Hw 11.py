# 3
class Student:
    __slots__ = ['name', 'age', 'grade']
    
    def __init__(self, name: str, age: int, grade: float):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"


def calculate_average_grade(students: list[Student]) -> float:
    """Вычисляет среднюю оценку студентов"""
    if not students:
        return 0.0
    total = sum(student.grade for student in students)
    return total / len(students)


students = [
    Student("Иван Иванов", 20, 4.5),
    Student("Петр Петров", 21, 3.8),
    Student("Анна Сидорова", 19, 5.0),
    Student("Мария Кузнецова", 20, 4.2),
    Student("Алексей Смирнов", 22, 4.7)
]

average_grade = calculate_average_grade(students)

print("Список студентов:")
for student in students:
    print(student)

print(f"\nСредняя оценка: {average_grade:.2f}")

try:
    students[0].address = "ул. Ленина, 1"
except AttributeError as e:
    print(f"\nПопытка добавить новый атрибут: {e}")


# 4
class Product:
    __slots__ = ['name', 'price', 'quantity']
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


def filter_products_by_price(products: dict[str, Product], threshold: float) -> list[str]:
    """Возвращает список названий товаров с ценой выше пороговой"""
    return [name for name, product in products.items() if product.price > threshold]


inventory = {
    "Ноутбук": Product("Ноутбук", 1200.50, 15),
    "Смартфон": Product("Смартфон", 800.30, 25),
    "Планшет": Product("Планшет", 450.75, 30),
    "Наушники": Product("Наушники", 150.20, 50),
    "Монитор": Product("Монитор", 350.90, 20)
}

threshold_price = 500.0
expensive_products = filter_products_by_price(inventory, threshold_price)

print("Весь инвентарь:")
for name, product in inventory.items():
    print(f"{name}: {product}")

print(f"\nТовары дороже {threshold_price}:")
for product_name in expensive_products:
    print(f"- {product_name} (Цена: {inventory[product_name].price})")

try:
    inventory["Ноутбук"].discount = 0.1
except AttributeError as e:
    print(f"\nПопытка добавить новый атрибут: {e}")
