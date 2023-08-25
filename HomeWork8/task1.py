# Напишите функцию, которая сереализует содержимое текущей директории в json-файл.
# В файле должен храниться список словарей, словарь описывает элемент внутри директории: имя, расширение, тип.
# Если элемент - директория, то только тип и имя.
# Пример результата для папки, где лежит файл test.txt и директория directory_test:
#
# directory_test/test.txt
#
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]

# C:\Users\Hp\Desktop\GB\PythonGB\HomeWorks\HomeWork8\task1.py    // моя директория с текущим файлом

import os
import json


current_file = os.path.realpath(__file__)
dir = current_file.split('\\')
print(dir)

dict = []
for el in dir:
    if '.' in el:
        name, extension = el.split('.')
        dict.append({'name': name, 'extension': '.' +
                    extension, 'type': 'file'})
    if ':' in el:
        dict.append({'name': el, 'type': 'disk'})
    else:
        dict.append({'name': el, 'type': 'directory'})
    print(f'el = {el}')
dict = dict[:-1]
print(dict)
with open('json_dict.json', 'w') as f:
    json.dump(dict, f, indent=4)
