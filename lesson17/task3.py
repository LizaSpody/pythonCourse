# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
# з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та
# операції порівняння між об'єктами класу Fraction


class Fraction:
    def __init__(self, topNumber, bottomNumber):
        self.topNumber = topNumber
        self.bottomNumber = bottomNumber

    def __add__(self, other):
        if self.bottomNumber % other.bottomNumber == 0:
            topNumber = int(self.bottomNumber / other.bottomNumber) * self.topNumber + other.topNumber
            bottomNumber = self.bottomNumber
        elif other.bottomNumber % self.bottomNumber == 0:
            topNumber = int(other.bottomNumber / self.bottomNumber) * self.topNumber + other.topNumber
            bottomNumber = other.bottomNumber
        else:
            bottomNumber = other.bottomNumber * self.bottomNumber
            topNumber = other.bottomNumber * self.topNumber + self.bottomNumber * other.topNumber
        return Fraction(topNumber, bottomNumber)


    def __sub__(self, other):
        if self.bottomNumber % other.bottomNumber == 0:
            topNumber = int(self.bottomNumber / other.bottomNumber) * self.topNumber - other.topNumber
            bottomNumber = self.bottomNumber
        elif other.bottomNumber % self.bottomNumber == 0:
            topNumber = int(other.bottomNumber / self.bottomNumber) * self.topNumber - other.topNumber
            bottomNumber = other.bottomNumber
        else:
            bottomNumber = other.bottomNumber * self.bottomNumber
            topNumber = other.bottomNumber * self.topNumber - self.bottomNumber * other.topNumber
        return Fraction(topNumber, bottomNumber)

    def __mul__(self, other):
        topNumber = self.topNumber * other.topNumber
        bottomNumber = self.bottomNumber * other.bottomNumber
        return Fraction(topNumber, bottomNumber)

    def __truediv__(self, other):
        topNumber = self.topNumber * other.bottomNumber
        bottomNumber = other.topNumber * self.bottomNumber
        return Fraction(topNumber, bottomNumber)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
    x - y == Fraction(1, 4)
    x * y == Fraction(1, 8)
    x / y == Fraction(4, 2)