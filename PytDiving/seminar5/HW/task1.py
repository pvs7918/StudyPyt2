# ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os.path

def get_path_params(file_full_path) -> tuple:

    # ищем последний \ в строке
    file_path = ""
    file_and_ext = ""
    for i in range(len(file_full_path)-1, 1, -1):
        if file_full_path[i] == '\\':
            file_path = file_full_path[:i+1]
            file_and_ext = file_full_path[i + 1:]
            break

    params = file_and_ext.split(sep=".")

    file_name = params[0]
    extension = params[1]

    return file_path, file_name, extension

cur_file_path = os.path.abspath(__file__)
print(f'\nИсходный путь: {cur_file_path}')
print(f'\nРезультат - кортеж: {get_path_params(cur_file_path)}')