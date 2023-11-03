# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def create_dict(start, end):
    my_dict = {}
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        my_dict[chr(i)] = i
    return my_dict


start, end = map(int, input('Введите два числа через пробел: ').split())
print(create_dict(start, end))
