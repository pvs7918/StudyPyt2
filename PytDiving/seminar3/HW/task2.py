# 2. Дан список повторяющихся элементов. Вернуть список с
# дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

import random

#формируем список с дублирующимися элементами
my_list = []
for i in range(10):
    my_list.append(random.randint(0, 5))

print(f'\nИсходный список: {my_list}')

unic_values = set(my_list)
dublicate_list = []

for val in unic_values:
    if my_list.count(val) > 1:
        dublicate_list.append(val)

print(f'\nСписок с дублирующимися элементами: {dublicate_list}')