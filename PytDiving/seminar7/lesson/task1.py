# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random


def fillFileByRandomNumbers(cnt_rows, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        for i in range(cnt_rows):
            int_n = random.randint(-1000, 1001)
            float_n = random.uniform(-1000, 1001)
            f.write(f'{int_n} | {float_n}\n')


fillFileByRandomNumbers(5, "task1_out.txt")