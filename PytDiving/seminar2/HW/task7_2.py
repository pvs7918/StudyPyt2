# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
import math


def my_fractions_add(a1: int, b1: int, a2: int, b2: int):
    """сложение обыкновенных дробей"""
    # находим наименьшее общее кратное для обоих знаменателей
    cur_lcm = math.lcm(b1, b2)

    ar = int((a1 * cur_lcm / b1)) + int(a2 * cur_lcm / b2)
    br = cur_lcm

    # сокращаем дробь если НОД числителя и знаменателя > 1
    cur_gcd = math.gcd(ar, br)
    if cur_gcd > 1:
        ar /= cur_gcd
        br /= cur_gcd

    return ar, br


def my_fractions_mul(a1, b1, a2, b2):
    """умножение обыкновенных дробей"""
    ar = a1 * a2
    br = b1 * b2
    # сокращаем дробь если НОД числителя и знаменателя > 1
    cur_gcd = math.gcd(ar, br)
    if cur_gcd > 1:
        ar /= cur_gcd
        br /= cur_gcd

    return ar, br


# print("Введите дробь 1:")
# a1 = int(input("Числитель:"))
# b1 = int(input("Знаменатель:"))
# print("Введите дробь 1:")
# a2 = int(input("Числитель:"))
# b2 = int(input("Знаменатель:"))

a1 = 13
b1 = 24
a2 = 55
b2 = 71

# решение с помощью своих методов
my_fr_res1 = my_fractions_add(a1, b1, a2, b2)
my_fr_res2 = my_fractions_mul(a1, b1, a2, b2)

# решение с помощью стандартной библиотеки - fractions.Fraction
fr1 = Fraction(a1, b1)
fr2 = Fraction(a2, b2)
fr_res1 = fr1 + fr2
fr_res2 = fr1 * fr2

print(f'Результат сложения дробей: {my_fr_res1[0]}/{my_fr_res1[1]}')
print(f'Проверка. Результат сложения дробей с помощью Fraction: {fr_res1}')
print(f'Результат умножения дробей: {my_fr_res2[0]}/{my_fr_res2[1]}')
print(f'Проверка. Результат умножения дробей с помощью Fraction: {fr_res2}')