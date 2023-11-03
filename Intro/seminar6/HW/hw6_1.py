# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate,
# list comprehension. Продолжение
# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
#
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]
#

from random import randint

N = int(input('Введите количество элементов списка: '))
up_value = int(input('Введите верхний предел значений для списка: '))

# создаем список случайных значений, применяя lambda-функцию, содержащую randint -
# функцию выбора случайного значения.
# вариант 1:
f = lambda x: randint(1, x + 1)
ls = [f(up_value) for i in range(N)]

# вариант 2 (через map()):
# ls = list(map(lambda x:randint(1, x + 1), [up_value for i in range(N)]))

# Дважды создаем список кортежей с помощью enumerate(ls),
# в результат помещаем значения val2,
# с условием - берем только те значения, которые больше предыдущих.
res_ls = [val2 for i1, val1 in enumerate(ls) for i2, val2 in enumerate(ls)
          if val2 > val1 and i2 == i1 + 1]

print(ls)
print(res_ls)