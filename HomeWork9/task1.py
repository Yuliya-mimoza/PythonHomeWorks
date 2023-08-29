# Создать декоратор для использования кэша.
# Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с агрументами,
# которые уже записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию. Кэш лучше хранить в json.

import json
from typing import Callable


def json_logging(func: Callable) -> Callable:
    try:
        with open(f'{func.__name__}.json', 'r') as data:
            result_list = json.load(data)
    except FileNotFoundError:
        result_list = []

    def wrapper(*args, **kwargs):
        dictionary: dict
        for dictionary in result_list:
            key = tuple(dictionary.get("args"))
            if key == args or key == kwargs:
                return dictionary
        result = func(*args, **kwargs)
        result_list.append({'args': args,
                            **kwargs,
                            'result': result})
        with open(f'{func.__name__}.json', 'w') as data:
            json.dump(result_list, data, indent=4)
        return result
    return wrapper


@json_logging
def sum_args(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    sum_args(1, 2, 3, 4)
