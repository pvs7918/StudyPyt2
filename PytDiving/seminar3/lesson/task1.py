# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

import random

my_list = []
for i in range(21):
    my_list.append(random.randint(0, 10))

print(my_list)

new_list = list(set(my_list))

print(new_list)

new_list2 = []
for i in my_list:
    if i not in new_list2:
        new_list2.append(i)

print(new_list2)