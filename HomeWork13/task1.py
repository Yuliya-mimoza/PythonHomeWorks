# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

class ErrorTriangle(Exception):
    def __str__(self) -> str:
        return f'С такими сторонами невозможно создать треугольник'


class ErrorSide(Exception):
    def __str__(self) -> str:
        return f'Стороны не могут принимать отрицательное значение'


class Triangle:
    def __init__(self, side_1: float, side_2: float, side_3: float) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if self.side_1 or self.side_2 or self.side_3 < 0:
            raise ErrorSide

    def check(self):
        B = 'Треугольник - равносторонний'
        C = 'Треугольник - равнобедренный'
        D = 'Треугольник разносторонний'
        if (self.side_1 > (self.side_2 + self.side_3))\
                or (self.side_2 > (self.side_1 + self.side_3))\
                or (self.side_3 > (self.side_1 + self.side_2)):
            raise ErrorTriangle
        elif self.side_1 == self.side_2 == self.side_3:
            return B
        elif self.side_1 == self.side_2\
                or self.side_2 == self.side_3\
                or self.side_3 == self.side_1:
            return C
        else:
            return D


t1 = Triangle(-5, 5, 5)
print(t1.check())
