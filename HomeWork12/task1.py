# Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву
#  и наличие только букв.

class Сheck_FIO:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, val):
        ALPHABET = {'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
                    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
                    'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а',
                    'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
                    'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
                    'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
        if val != val.capitalize():
            raise ValueError('Первая буква не заглавная! ')
        for el in val:
            if el not in ALPHABET:
                raise ValueError(
                    f'Наличие недопустимого символа в ФИО: "{el}"')


class Student:
    surname = Сheck_FIO()
    name = Сheck_FIO()
    patronymic = Сheck_FIO()

    def __init__(self, surname, name, patronymic) -> None:
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self) -> str:
        return f"_____Студент_____\nфамилия:  {self.surname}\nимя:      {self.name}\nотчество: {self.patronymic}"


s1 = Student('Иванов', 'Иван', 'Иванович')
print(s1)
