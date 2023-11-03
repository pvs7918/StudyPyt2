# https://zaochnik.com/spravochnik/matematika/delimost/naimenshee-obschee-kratnoe-nok/

# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd


print("Введите два числа: ")
a = int(input("a = "))
b = int(input("b = "))

def nok (first, second):
    return(first*second) // gcd(first, second)
print(nok(a,b))
