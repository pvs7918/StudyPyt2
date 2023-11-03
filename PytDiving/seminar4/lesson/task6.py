# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def calc_summ(lst, st, end):
    if st > end:
        st, end = end, st  # меняем местами индекс начала и конца если они неправильно указаны
    if st < 0:
        st = 0
    if end > len(lst) - 1:
        end = len(lst) - 1

    # #вариант 1
    # filtered_list = []
    # #формируем результирующий список, от указанных начала и конца
    # for i in range(st, end+1):
    #     filtered_list.append(lst[i])
    # print(f'Отладка. Промежуточный список: {filtered_list}')
    # return sum(filtered_list)

    # вариант 2
    print(f'Отладка. Промежуточный список: {lst[st:end + 1]}')
    return sum(lst[st:end + 1])


src_list = [1, 4, 5, 10, 3, 2, 7, 9, 2, 6]
start_ind = 12
end_ind = 1

print(calc_summ(src_list, start_ind, end_ind))
