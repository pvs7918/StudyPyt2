# Напишите следующие функции:
# ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения
#  с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции
#  в json файл.
from random import randint
import csv
import json


# реализация без декораторов. task1_decor.py - тоже самое по сути, но через декораторы

def solving_quad_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if a == 0:
        # варианты неполного квадратного уравнения
        if b == 0:
            return None
        else:
            return -c / b
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b
    else:
        return None


def gen_csv(cnt: int, n_min, n_max):
    with open('task1.csv', 'w', newline='', encoding='utf-8') as f1:
        csv_write = csv.DictWriter(f1,
                                   fieldnames=["a", "b", "c"],
                                   dialect='excel',
                                   quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        dict = {}
        for i in range(cnt):
            dict["a"] = randint(n_min, n_max + 1)
            dict["b"] = randint(n_min, n_max + 1)
            dict["c"] = randint(n_min, n_max + 1)
            csv_write.writerow(dict)
    return True


def read_csv_and_decide_equations():
    with open('task1.csv', 'r', newline='', encoding='utf-8') as f1:
        csv_file = csv.reader(f1, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        res_dict = {}
        for i, row in enumerate(csv_file):
            if i != 0:
                res_dict[str(row)] = solving_quad_equation(row[0], row[1], row[2])
    return res_dict


def save_to_json(res_dict):
    with open('task1.json', 'w', encoding='utf-8') as f1:
        json.dump(res_dict, f1, ensure_ascii=False, indent=4)


def main():
    # game = outer()
    # game()

    # 1. генерация csv файла с коэффициентами a,b,c
    gen_csv(cnt=randint(100, 1001), n_min=-10, n_max=10)
    res_dict = read_csv_and_decide_equations()
    save_to_json(res_dict)


if __name__ == '__main__':
    main()
