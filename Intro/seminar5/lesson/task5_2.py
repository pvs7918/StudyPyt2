# 2. Дан список чисел. Создайте список, в который попадают числа,
#    описываемые возрастающую последовательность.
#    Порядок элементов менять нельзя.

from random import choices


def sequ(num):
    if num < 1:
        return []
    return choices(range(num * 2), k=num)


def all_sets(num_list):
    new_list = []
    for k in range(len(num_list)):
        n = num_list[k]
        temporary = [n]
        for i in range(k + 1, len(num_list)):
            if num_list[i] > n:
                n = num_list[i]
                temporary.append(n)
        if len(temporary) > 1:
            new_list.append(temporary)

    return new_list


list_nums = sequ(int(input()))
print(list_nums)
print(all_sets(list_nums))