# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра. (Например: Треугольник дз1, дроби дз2)

class Triangle:
    def __init__(self, side_1: float, side_2: float, side_3: float) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def check(self):
        A = 'Треугольника с такими сторонами не существует! '
        B = 'Треугольник - равносторонний'
        C = 'Треугольник - равнобедренный'
        D = 'Треугольник разносторонний'
        if (self.side_1 > (self.side_2 + self.side_3))\
                or (self.side_2 > (self.side_1 + self.side_3))\
                or (self.side_3 > (self.side_1 + self.side_2)):
            return A
        elif self.side_1 == self.side_2 == self.side_3:
            return B
        elif self.side_1 == self.side_2\
                or self.side_2 == self.side_3\
                or self.side_3 == self.side_1:
            return C
        else:
            return D


t1 = Triangle(5, 5, 5)
print(t1.check())
