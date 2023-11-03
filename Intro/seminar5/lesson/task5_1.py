# 1. Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.


from random import choice


def sequ(num):
    if num < 1:
        return []

    num_list = list(range(num + 1))
    num_list.remove(choice(num_list))
    return num_list


def lostie(num_list):
    for i in range(1, len(num_list)):
        if num_list[i - 1] != num_list[i] - 1:
            return num_list[i] - 1
    return -1


list_nums = sequ(int(input()))
print(list_nums)
print(lostie(list_nums))
