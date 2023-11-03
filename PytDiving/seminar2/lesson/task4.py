# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
from decimal import Decimal, getcontext

getcontext().prec = 32
def circle(diametr):
    result = Decimal(diametr * math.pi)
    area = Decimal(((diametr/2)**2)*math.pi)
    return result, area

diametr = float(input("Введите диаметр: "))
print(circle(diametr))