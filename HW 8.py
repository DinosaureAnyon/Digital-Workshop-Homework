import math


class Fraction:
    def __new__(cls, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        
        common_divisor = math.gcd(abs(numerator), abs(denominator))
        simplified_num = numerator // common_divisor
        simplified_den = denominator // common_divisor

        if simplified_den < 0:
            simplified_num *= -1
            simplified_den *= -1

        key = (simplified_num, simplified_den)
        
        if not hasattr(cls, '_instances'):
            cls._instances = {}
            
        if key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, numerator: int, denominator: int = 1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")

        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        common_divisor = math.gcd(abs(numerator), abs(denominator))
        simplified_num = numerator // common_divisor
        simplified_den = denominator // common_divisor

        if simplified_den < 0:
            simplified_num *= -1
            simplified_den *= -1

        if not hasattr(self, '_numerator'):
            self._numerator = simplified_num
            self._denominator = simplified_den

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    @property
    def value(self) -> float:
        return round(self._numerator / self._denominator, 3)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_num = self._numerator * other.denominator + other.numerator * self._denominator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_num = self._numerator * other.denominator - other.numerator * self._denominator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_num = self._numerator * other.numerator
        new_den = self._denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_num = self._numerator * other.denominator
        new_den = self._denominator * other.numerator
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return (self._numerator == other.numerator and 
                self._denominator == other.denominator)

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return (self._numerator * other.denominator < 
                other.numerator * self._denominator)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __hash__(self):
        return hash((self._numerator, self._denominator))

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    @classmethod
    def from_string(cls, fraction_str: str):
        try:
            num, den = map(int, fraction_str.split('/'))
            return cls(num, den)
        except (ValueError, IndexError):
            raise ValueError("Invalid fraction format. Use 'a/b'")

    @staticmethod
    def is_proper(fraction) -> bool:
        """Проверяет, является ли дробь правильной (числитель < знаменатель)"""
        return abs(fraction.numerator) < abs(fraction.denominator)


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
f3 = Fraction(2, 4)

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1.value)

print(f1 == f3)
print(f1 is f3)
print(f1 < f2)
print(f1 > f2)
print(f1 <= f3)  
print(f1 >= f3)

print(hash(f1) == hash(f3))

try:
    Fraction(1, 0)
except ZeroDivisionError as e:
    print(e)

f4 = Fraction.from_string("2/3")
print(f4)

print(Fraction.is_proper(f1))
print(Fraction.is_proper(f2))
print(Fraction.is_proper(f1 + f2))
