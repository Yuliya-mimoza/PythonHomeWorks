# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions


def sum(a1: int, b1: int, a2: int, b2: int):  # функция нахождения суммы дробей
    if b1 == b2:
        a = a1 + a2
        b = b1 = b2
    else:
        a = (a1*b2)+(a2*b1)
        b = b1*b2
    return funct(int(a), int(b))


def comp(a1: int, b1: int, a2: int, b2: int):  # нахождения произведения дробей
    a = a1 * a2
    b = b1 * b2
    return funct(int(a), int(b))


def funct(a: int, b: int):  # функция сокращения дроби
    if a < b:
        min = a
    else:
        min = b
    for i in range(min, 1, -1):
        if a % i == 0 and b % i == 0:
            a /= i
            b /= i
    return (f'{int(a)}/{int(b)}')


a1, b1 = map(int, input("Введите первую дробь вида “a/b”: ").split("/"))
a2, b2 = map(int, input("Введите вторую дробь вида “a/b”: ").split("/"))

print(f"Сумма дробей равна: {sum(a1, b1, a2, b2)}")
print(f"Произведение дробей равно: {comp(a1, b1, a2, b2)}")

# проверка кода с использованием модуля fractions
x = fractions.Fraction(a1, b1)
y = fractions.Fraction(a2, b2)
print(f"Сумма дробей с использованием модуля 'fractions' равна: {x+y}")
print(f"Произведение дробей с использованием модуля 'fractions' равно: {x*y}")
