# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

def gonext(number, system_sch):
    result = 0
    ost = 0
    rez_string = ''
    while True:
        result = number // system_sch
        ost = number % system_sch
        if result < system_sch:
            rez_string += str(ost) + str(result)
            break
        else:
            number = result
            rez_string += str(ost)
    return rez_string[::-1]

numb = int(input('Введите целое число: '))

print(gonext(numb, 8))