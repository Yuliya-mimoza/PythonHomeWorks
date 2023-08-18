# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

def real_date(data: str):
    MAXDAY = 31
    MAXMONTH = 12
    MAXYEAR = 9999
    MIN = 1
    MONTH_FEB = 2
    MONTH_APR = 4
    MONTH_JUN = 6
    MONTH_SEP = 9
    MONTH_NOV = 11
    MAXDAY_FEB = 29
    d, m, y = data.split('.')
    day = int(d)
    month = int(m)
    year = int(y)
    print(day, month, year)
    if day > MAXDAY or day < MIN\
            or month > MAXMONTH or month < MIN\
            or year > MAXYEAR or year < MIN:
        return False
    else:
        if _leap_year(year) is True\
                and month == MONTH_FEB\
                and day <= MAXDAY_FEB:
            return True
        else:
            if month == MONTH_APR and day == MAXDAY-MIN\
                    or month == MONTH_JUN and day <= MAXDAY-MIN\
                    or month == MONTH_SEP and day <= MAXDAY-MIN\
                    or month == MONTH_NOV and day <= MAXDAY-MIN:
                return True
            else:
                return False


def _leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print("Этот год високосный... ")
        return True
    else:
        print("Этот год не високосный... ")
        return False


data = input("Введите дату в формате DD.MM.YYYY: ")

if __name__ == '__main__':
    if real_date(data) is True:
        print("Такая дата возможна")
    else:
        print("Такая дата невозможна")
