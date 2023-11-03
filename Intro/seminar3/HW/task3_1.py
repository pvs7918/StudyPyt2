# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# ________________________________________
# in
# 4
# out
# [4, 2, 4, 9]
# 8
# ________________________________________

from random import sample


def GetSampleList(listLen):
    if not listLen > 0:
        print('Длина списка задана неверно')
        return []
    # sample берет из range (длиной n*2) n случайных значений и возвращет их списком
    return sample(range(1, listLen * 2), listLen)


def FindInList_OddPosSum(ls):
    if not ls:
        return "список не задан"
    n = len(ls)
    summ = 0
    for i in range(0, n, 2):  # нечетные позиции это значит чётные индексы. 2 это шаг иттерации
        summ += ls[i]
    return summ


N = int(input('Введите количество элементов списка: '))
ls = GetSampleList(N)
if ls:
    print(ls)
    print(f'Сумма нечетных элементов списка равна: {FindInList_OddPosSum(ls)}')
