# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

#from math import sqrt
import math

print("Введите коэффициенты квадратного уравнения")
a = float(input("а = "))
b = float(input("b = "))
c = float(input("c = "))

d = b**2 - 4 * a*c
sqrtd1 = d**0.5

with open("temp.txt", "a", encoding="utf-8") as output:
    output.write(f"уравнение: {a}*x^2 + {b}*x + {c}")
    if d > 0 and a:
        x1 = (-b + sqrtd1) / (2*a)
        x2 = (-b - sqrtd1) / (2*a)
        output.write(f"корни уравнения: {x1, x2 }")
    elif (int(d)) == 0:
        x = -b / (2*a)
        output.write(f"единственный корень: {x}")
    else:
        output.write("корней нет")
