# 1
import math


class Fraction:
    def __new__(cls, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        return super().__new__(cls)

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

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1.value)

try:
    Fraction(1, 0)
except ZeroDivisionError as e:
    print(e)

f3 = Fraction.from_string("2/3")
print(f3)

print(Fraction.is_proper(f1))
print(Fraction.is_proper(f2))
print(Fraction.is_proper(f1 + f2))

# 2
from fractions import Fraction
from copy import deepcopy


class FractionMatrix:
    def __new__(cls, matrix):
        if not all(isinstance(row, list) for row in matrix):
            raise ValueError("Matrix must be a list of lists")
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("All rows must have the same length")
        return super().__new__(cls)

    def __init__(self, matrix):
        self._validate_matrix(matrix)
        self.matrix = [
            [Fraction(item.numerator, item.denominator) if isinstance(item, Fraction) else Fraction(item) for item in
             row] for row in matrix]
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    @staticmethod
    def _validate_matrix(matrix):
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise TypeError("Matrix must be a list of lists")
        if not matrix:
            raise ValueError("Matrix cannot be empty")
        if any(not all(isinstance(item, (Fraction, int)) for item in row) for row in matrix):
            raise TypeError("All matrix elements must be Fractions or integers")

    @property
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant can only be calculated for square matrices")
        return self._calculate_determinant(self.matrix)

    def _calculate_determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = Fraction(0)
        for col in range(n):
            minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
            sign = (-1) ** col
            det += sign * matrix[0][col] * self._calculate_determinant(minor)
        return det

    def __add__(self, other):
        if not isinstance(other, FractionMatrix):
            raise TypeError("Can only add FractionMatrix to FractionMatrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return FractionMatrix(result)

    def __sub__(self, other):
        if not isinstance(other, FractionMatrix):
            raise TypeError("Can only subtract FractionMatrix from FractionMatrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")

        result = [
            [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return FractionMatrix(result)

    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            result = [
                [self.matrix[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return FractionMatrix(result)
        elif isinstance(other, FractionMatrix):
            if self.cols != other.rows:
                raise ValueError("Number of columns in first matrix must match number of rows in second matrix")

            result = [
                [
                    sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols))
                    for j in range(other.cols)
                ]
                for i in range(self.rows)
            ]
            return FractionMatrix(result)
        else:
            raise TypeError("Can only multiply by scalar or FractionMatrix")

    def transpose(self):
        return FractionMatrix([
            [self.matrix[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])

    @classmethod
    def identity(cls, size):
        if size <= 0:
            raise ValueError("Size must be positive")
        return cls([
            [Fraction(1 if i == j else 0) for j in range(size)]
            for i in range(size)
        ])

    def __str__(self):
        max_len = max(
            len(str(element)) for row in self.matrix for element in row
        )
        return "[\n" + "\n".join(
            "  [" + ", ".join(f"{str(element):>{max_len}}" for element in row) + "]"
            for row in self.matrix
        ) + "\n]"

    def __repr__(self):
        return f"FractionMatrix({self.matrix})"



if __name__ == "__main__":
    m1 = FractionMatrix([
        [Fraction(1, 2), Fraction(1, 3)],
        [Fraction(2, 5), Fraction(3, 4)]
    ])
    m2 = FractionMatrix([
        [Fraction(1, 3), Fraction(2, 3)],
        [Fraction(1, 2), Fraction(2, 5)]
    ])

    print("Matrix 1:")
    print(m1)
    print("\nMatrix 2:")
    print(m2)

    print("\nAddition:")
    print(m1 + m2)

    print("\nMultiplication:")
    print(m1 * m2)

    print("\nTranspose of m1:")
    print(m1.transpose())

    print("\nDeterminant of m1:")
    print(m1.determinant)

    print("\nIdentity matrix 3x3:")
    print(FractionMatrix.identity(3))