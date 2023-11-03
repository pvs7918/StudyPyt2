# 2. Напишите функцию группового переименования файлов. Она должна:
# 3. Принимать параметр желаемое конечное имя файлов.
#  При переименовании в конце имени добавляется порядковый номер.
# 4. Принимать параметр количество цифр в порядковом номере.
# 5. Принимать параметр расширение исходного файла. Переименование должно работать
# только для этих файлов внутри каталога.
# 6. Принимать параметр расширение конечного файла.
# 7. Принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое
# конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def group_rename_files(dir: str, res_filename: str, number_digits: int,
                       src_ext: str, res_ext: str,
                       name_min, name_max):
    """Функция берет файлы в исходном каталоге dir.
    Переименовывает их согласно следующему правилу:
    Например для диапазона[3, 6] берутся буквы с 3 по 6
    из исходного имени файла.
    К ним прибавляется желаемое конечное имя, если оно передано.
    Далее счётчик файлов и расширение."""

    if not os.path.exists(dir):
        print('Исходный каталог отсутсвует')
        return False

    # проверяем допустимость значений параметров
    if name_min > name_max:
        name_min, name_max = name_max, name_min
    if name_min < 0:
        name_min = 0

    # счётчик файлов
    counter = 1

    # получаем список файлов для указанного каталога dir
    for dir_path, dir_name, file_name in os.walk(dir):
        for cur_file in file_name:
            parts = cur_file.split(".")
            cur_name = parts[0]
            cur_ext = parts[1]
            res_file = ''
            if cur_ext == src_ext:
                # в обработку берем только файлы с расширением src_ext
                if name_max > len(cur_name):
                    res_file += cur_name[name_min:]
                else:
                    res_file += cur_name[name_min:name_max+1]
                # добавляем желаемое конечное имя файла
                res_file += res_filename
                # добавляем порядковый номер с нужным количеством цифр
                if number_digits <= len(str(counter)):
                # вычисляем количество нулей перед порядковым номером
                    cur_zero = 0
                else:
                    cur_zero = number_digits - len(str(counter))

                res_file += '0' * cur_zero + str(counter) + '.' + res_ext
                #переименовываем файл
                cur_file = os.path.join(dir, cur_file)
                res_file = os.path.join(dir, res_file)
                os.rename(cur_file, res_file)
                counter += 1

#print(group_rename_files('test', 'copy', 2, 'md', 'doc', 2, 3))
print(group_rename_files('test', 'qwert', 1, 'md', 'txt', 1, 4))
