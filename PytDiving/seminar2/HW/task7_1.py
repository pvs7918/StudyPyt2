# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.


def dec_to_hex(numb: int) -> str:
    # функция преобразует целое число в шестнадцатеричное строковое представление
    base = 16  # основание системы счисления
    res = ''
    remainder = numb
    while remainder > 0:
        digit = remainder % base
        if digit < 10:
            cur_hex_digit = str(digit)
        else:
            cur_hex_digit = chr(55 + digit)  #символ A - код символа - 65
        res = cur_hex_digit + res  # символ добавляем слева
        remainder = remainder // base

    if res == '':
        res.lower = '0'

    return f'0x{res.lower()}'


while True:
    numb = int(input("Введите целое число: "))
    print(f'{numb=}, {dec_to_hex(numb)=}, {hex(numb)=}')
