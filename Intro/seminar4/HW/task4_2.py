# 2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# ________________________________________
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# ________________________________________
# in
# 650
# out
# [2, 5, 5, 13]
# ________________________________________

def GetSimpleMultipliers(N):
    # сформировать список простых чисел от 2 до N
    if N < 2:
        return []

    simpleNums = []
    for i in range(2, N + 1):
        boolSimple = True
        for k in range(2, i):
            if (i % k) == 0:
                boolSimple = False
                break
        if boolSimple:
            simpleNums.append(i)
    return simpleNums


def FindSimpleMultiForNumber(N):
    # функция находит список простых множителей числа
    simpNums = GetSimpleMultipliers(N)
    remainder = N
    list_res = []

    while remainder > 1:
        for curSimp in simpNums:
            if remainder % curSimp == 0:
                list_res.append(curSimp)
                remainder //= curSimp
                break

    return list_res

N = int(input("Введите натуральное число N: "))
print(FindSimpleMultiForNumber(N))



#список простых множителей числа (вывод для проверки)
#print(GetSimpleMultipliers(N))

