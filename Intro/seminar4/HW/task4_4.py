# 4.* Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (от 0 до 10) многочлена, записать в файл полученный
# многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# ________________________________________
# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import randint, choice


def GetEquationString(k):
    сoef = []
    sign = ['+', '-']
    for i in range(k + 1):
        tmp = randint(0, 11)
        sng = choice(sign)
        if tmp != 0:
            if i == 0:
                сoef.insert(0, f'{sng} {tmp}')
            elif i == k:
                if sng == '+':
                    сoef.insert(0, f'{tmp}*x^{i}')
                else:
                    сoef.insert(0, f'{sng} {tmp}*x^{i}')
            else:
                сoef.insert(0, f'{sng} {tmp}*x^{i}')

    return ' '.join(сoef) + ' = 0\n'


def WriteEquationsInFile(countEq, Degree):
    FileName = 'equations.txt'
    with open(FileName, 'w', encoding='utf8') as f1:
        f1.write('Список уравнений:\n')
        for i in range(countEq):
            f1.write(GetEquationString(Degree))
    return f'Файл {FileName} записан!'


k = int(input('Введите степень k: '))
N = int(input('Введите количество уравнений: '))
if k > 0 and N > 2:
    Status = WriteEquationsInFile(N, k)
    print(Status)
else:
    print('Ошибка! Введите натуральное число степени больше 0 и количество уравнений больше 2')
