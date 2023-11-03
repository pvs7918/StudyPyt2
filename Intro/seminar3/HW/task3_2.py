# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# ________________________________________
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
# ________________________________________

from random import randint


def GetSampleList(listLen, topNum):
    if not listLen > 0:
        print('Длина списка задана неверно')
        return []
    ls = []
    for i in range(listLen):
        ls.append(randint(1, topNum))
    return ls

def CalcSumsOfPairs(ls):
    len_ls = len(ls)
    summs = []
    for i in range(len_ls // 2):
        summs.append(ls[i] + ls[len_ls - i - 1])
    if len_ls % 2 == 1:
        summs.append(ls[len_ls // 2])
    return summs

N = int(input('Введите количество элементов списка: '))
ls = GetSampleList(N, 10)
if ls:
    print(ls)
    print(CalcSumsOfPairs(ls))

