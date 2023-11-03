# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# ________________________________________
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988
# ________________________________________

from decimal import Decimal


def GetNumberFixedAccuracy(x, accur):
    #Возвращает число x с заданной точностью accur
    return Decimal(x).quantize(Decimal(accur))


SrcNumb = input('Enter a real number: ')
Accur = input("Enter the required accuracy '0.0001': ")
print(f'Result: {GetNumberFixedAccuracy(SrcNumb, Accur)}')
