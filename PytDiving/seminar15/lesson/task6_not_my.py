# 📌 Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя
# логирование.


from collections import namedtuple
import os
import logging
import sys


def directory_info(path=os.getcwd()):
    info = os.listdir(path)

    Info = namedtuple("Info", ['name', 'extension', 'catalog_flag', 'parent_directory'])
    print(info)
    logging.basicConfig(filename='DIRECTORY_INFO.log.', filemode='a', encoding='utf-8', level=logging.INFO)
    for i in info:
        i = os.path.join(path, i)
        if os.path.isfile(i):
            new_info_ob = Info(*i.split("\\")[-1].split("."), False, path)

            logging.info(new_info_ob)
        if os.path.isdir(i):
            new_info_ob = Info(i.split("\\")[-1], None, True, path)
            logging.info(new_info_ob)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_info(sys.argv[1])
    else:
        directory_info()