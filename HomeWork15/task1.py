import logging

FORMAT = '{levelname} - {asctime} {msg}'

logging.basicConfig(filename='logger.log', encoding='utf-8',
                    level=logging.INFO, filemode='w', format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def logging_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(
            f'Функция: "{func.__name__}", с аргументами {args}{kwargs}')
        return result
    return wrapper


@logging_deco
class ErrorTriangle(Exception):
    def __str__(self) -> str:
        return logger.error(f'С такими сторонами невозможно создать треугольник')


@logging_deco
class ErrorSide(Exception):
    def __init__(self, *args) -> None:
        self.value = []
        self.value = args
        self.new_value = []
        for el in self.value:
            if int(el) < 0:
                self.new_value.append(el)

    def __str__(self) -> str:
        return logger.error(f"Стороны не могут принимать отрицательное значение: {self.new_value}")


class Triangle:
    def __init__(self, side_1: float, side_2: float, side_3: float) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if self.side_1 < 0 or self.side_2 < 0 or self.side_3 < 0:
            raise ErrorSide(side_1, side_2, side_3)

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


t1 = Triangle(-15, 5, -3)
print(t1.check())
