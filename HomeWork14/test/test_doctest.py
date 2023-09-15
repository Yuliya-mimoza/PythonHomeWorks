# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задание в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.
# (Просьба, тесты хранить в разных папках, отдельно под pytest, отдельно под unittest и т.д.)

class ErrorTriangle(Exception):
    def __str__(self) -> str:
        return f'С такими сторонами невозможно создать треугольник'


class ErrorSide(Exception):
    def __str__(self) -> str:
        return f'Стороны не могут принимать отрицательное значение:'


class Triangle:
    def __init__(self, side_1: float, side_2: float, side_3: float) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if self.side_1 < 0 or self.side_2 < 0 or self.side_3 < 0:
            raise ErrorSide(side_1, side_2, side_3)

    def check(self):
        """
        >>> Triangle(3, 6, 6).check()
        'Треугольник - равнобедренный'

        >>> Triangle(5, 5, 5).check()
        'Треугольник - равносторонний'

        >>> Triangle(4, 5, 6).check()
        'Треугольник - разносторонний'

        """
        B = 'Треугольник - равносторонний'
        C = 'Треугольник - равнобедренный'
        D = 'Треугольник - разносторонний'
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


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
