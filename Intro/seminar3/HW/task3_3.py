# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# ________________________________________
# in
# 11
# out
# 1011
# ________________________________________

def ConvertDecToBin(srcNum):
    # формируем список бинарного представления числа
    resBin = []
    while srcNum:
        resBin.append(srcNum % 2)
        srcNum //= 2
    res = 0
    for i in range(len(resBin)):
        # в десятичное число помещаем двоичное представление. Поэтому умножение на 10
        res += resBin[i] * 10 ** i
    return res


srcNum = int(input('Введите десятичное число: '))
print(ConvertDecToBin(srcNum))