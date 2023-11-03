# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# ________________________________________
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform


def GetSampleFloatList(listLen, downFloatNum, topFloatNum):
    if not listLen > 0:
        print('Длина списка задана неверно')
        return []
    ls = []
    for i in range(listLen):
        # округляем до 2-х знаком после запятой вещественные числа
        ls.append(float(round(uniform(downFloatNum, topFloatNum), 2)))
    return ls


def FindMinMaxFractPart(ls):
    if not ls:
        return None
    len_ls = len(ls)
    minFr = ls[0] % 1
    maxFr = ls[0] % 1

    for i in range(len_ls):
        curFr = ls[i] % 1
        if curFr < minFr:
            minFr = curFr
        if curFr > maxFr:
            maxFr = curFr
    return minFr, maxFr


N = int(input('Введите количество элементов списка: '))
ls = GetSampleFloatList(N, 1, 10)
print(ls)
res = FindMinMaxFractPart(ls)
if not res:
    print('Список не был задан. Выполнение программы прервано')
else:
    minval, maxval = res
    print(f'Min: {minval:.2f}, Max: {maxval:.2f}. Difference: {maxval - minval:.2f}')
