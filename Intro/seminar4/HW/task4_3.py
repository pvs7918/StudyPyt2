# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной
# последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# ________________________________________
# in
# -1
# out
# Negative value of the number of numbers!
# []
# ________________________________________
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
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

def DelDublicatesInLlist(ls):
    len_ls = len(ls)
    doubleInd = [] #список индексов дублирующихся элементов
    res = []

    #находим индексы дублирующихся элементов
    for i in range(len_ls):
        if not (i in doubleInd):
            boolDouble = False
            for k in range(i+1, len_ls):
                if ls[i] == ls[k]:
                    doubleInd.append(k)
                    boolDouble = True
            if boolDouble:
                doubleInd.append(i)
    doubleInd.sort()

    for i in range(len_ls):
        if not (i in doubleInd):
            res.append(ls[i])
    return res


N = int(input('Введите количество элементов списка: '))
ls = GetSampleList(N, 10)
if ls:
    print(ls)
    print(DelDublicatesInLlist(ls))