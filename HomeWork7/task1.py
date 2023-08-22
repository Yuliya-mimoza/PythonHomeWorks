# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Чтобы записать байты можно использовать список с числами и функцию bytes

from random import choice, randint

CONSONANTS = 'eyuioaqwrtpsdfghjklzxcvbnm'
MIN_LEN_NAME = 6
MAX_LEN_NAME = 30
MIN_BYTES = 256
MAX_BYTES = 4096
COUNT_FILES = 42


def name_gen():
    res = ''
    for _ in range(randint(MIN_LEN_NAME, MAX_LEN_NAME)):
        res += choice(CONSONANTS)
    return res


def creating_file():
    with open(name_gen(), 'w') as names_file:
        for _ in range(randint(MIN_BYTES, MAX_BYTES)):
            result = bytes(randint(1, 100))
        names_file.write(str(result))


def gen_random_files():
    for _ in range(COUNT_FILES):
        creating_file()


if __name__ == '__main__':
    gen_random_files()
