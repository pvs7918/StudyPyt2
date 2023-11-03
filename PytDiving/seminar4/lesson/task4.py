# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

my_list = [5, 1, 34, 76, 12, 56, 3, 1, 92]


def sorted_list(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)

sorted_list(my_list)

print(my_list)