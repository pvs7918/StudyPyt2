# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

a = float(input('Введите число: '))
remainder = a
stra = str(a)

# определяем позицию точки в строке
pointpos = stra.rfind('.')

# уходим от дробной части, домножая на степень числа 10 - количества символов после запятой)
if pointpos >= 0:
    remainder *= 10 ** (len(stra) - pointpos - 1)

summary = 0
while remainder > 0:
    curDigit = remainder % 10
    summary += curDigit
    remainder //= 10

print(f'{a} -> {summary:.0f}')
