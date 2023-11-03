# 📌 Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.

# моё решение

import os
import logging
import sys
from collections import namedtuple
from pathlib import Path


def read_folder(source_folder_name=os.path.curdir):


    info = namedtuple("Info", ['name', 'ext', 'folder', 'parent'])

    logging.basicConfig(filename='task6.log', filemode='w',
                        encoding='utf-8', level=logging.INFO)

    # полной путь к сканируемому каталогу
    source_dir_path = os.path.join(os.getcwd(), source_folder_name)
    res_list = []  # результирующий список словарей

    # Добавляем исходный каталог
    inf = info(source_folder_name, '', 'True', str(Path(source_dir_path).parent))
    res_list.append(inf)

    # Обход подкаталогов и файлов с помощью os.walk
    for dir_path, dir_names, file_names in os.walk(source_dir_path):
        # получаем списки подкаталогов dir_names и файлов file_name
        for cur_dir in dir_names:
            inf = info(cur_dir, '', 'True', dir_path)
            res_list.append(inf)

        for cur_file in file_names:
            parts = cur_file.split('.')
            inf = info(parts[0], parts[1], 'False', dir_path)
            res_list.append(inf)

    # запись в log
    for rec in res_list:
        logging.info(rec)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        read_folder(sys.argv[1])
    else:
        read_folder()

    # Для запуска с параметрами в IDE PyCharm: Run\Run...\Edit Configurations...\Parameters
    # там прописать параметры через пробел, которые помещаются в sys.argv начиная с 1-го элемента