# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def hex_func(number: int, number_sys: int = 16):
    hex_number = ""
    list_hex_sys = ["A", "B", "C", "D", "E", "F"]
    while number != 0:
        result = str(number % number_sys)
        match result:
            case "10":
                result = list_hex_sys[0]
            case "11":
                result = list_hex_sys[1]
            case "12":
                result = list_hex_sys[2]
            case "13":
                result = list_hex_sys[3]
            case "14":
                result = list_hex_sys[4]
            case "15":
                result = list_hex_sys[5]

        hex_number = result + hex_number
        number //= number_sys

    return hex_number


number = int(input("Введите число: "))

print(
    f"Число в шестнадцатеричной системе через мою функцию: {hex_func(number)}")

print(
    f"Число в шестнадцатеричной системе через функцию 'hex': {hex(number)[2:]}")
