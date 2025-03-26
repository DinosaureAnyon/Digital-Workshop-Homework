# 2
class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    @staticmethod
    def __is_password_secure(password: str) -> bool:
        return len(password) >= 6

    @classmethod
    def create_default_user(cls, username: str):
        default_password = "defaultSecurePassword123"
        return cls(username, default_password)

    def get_username(self) -> str:
        return self.__username

    def set_password(self, new_password: str) -> None:
        if not self.__is_password_secure(new_password):
            raise ValueError("Пароль слишком короткий (минимум 6 символов)")
        self.__password = new_password
        print("Пароль успешно изменён")

user = User.create_default_user("Alice")
print(user.get_username())

try:
    user.set_password("12345")
except ValueError as e:
    print(e)

user.set_password("securePass")

# 3
from datetime import datetime

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.__title = title
        self.__author = author
        self.__year = year

    @staticmethod
    def __is_valid_year(year: int) -> bool:
        current_year = datetime.now().year
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_default_year(cls, title: str, author: str):
        default_year = 2024
        return cls(title, author, default_year)

    def get_info(self) -> str:
        return f'"{self.__title}", автор: {self.__author}, год: {self.__year}'

book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())

book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())

try:
    book3 = Book("Test Book", "Test Author", 3000)
except ValueError as e:
    print(e)