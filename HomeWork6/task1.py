# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

def real_date(data: str):
    MAXDAY = 30
    MAXMONTH = 12
    MAXYEAR = 9999
    MIN = 1
    MONTH_FEB = 2
    MONTH_MARCH = 3
    MONTH_MAY = 5
    MONTH_JULY = 7
    MONTH_AUG = 8
    MONTH_OCTB = 10
    MONTH_DEC = 12
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
            if month == MIN and day == MAXDAY\
                    or month == MONTH_MARCH and day <= MAXDAY+MIN\
                    or month == MONTH_MAY and day <= MAXDAY+MIN\
                    or month == MONTH_JULY and day <= MAXDAY+MIN\
                    or month == MONTH_AUG and day <= MAXDAY+MIN\
                    or month == MONTH_OCTB and day <= MAXDAY+MIN\
                    or month == MONTH_DEC and day <= MAXDAY+MIN:
                return True
            else:
                return True


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
