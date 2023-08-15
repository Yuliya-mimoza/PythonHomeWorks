# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt

# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

def the_path_to_the_file(str):
    res = str.split('/')
    *a, b = res
    c, d = b.split('.')
    a1 = "/".join(a)+'/'
    d = '.'+d
    return a1, c, d


stroka = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
print(the_path_to_the_file(stroka))
