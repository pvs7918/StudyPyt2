# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import random
from random import randint, randbytes, sample, choice
from string import ascii_letters
import os


def random_extension(list_ext: list[str]) -> str:
    return random.choice(list_ext)


def create_files(extension: list[str], dir: str, min_name: int = 6, max_name: int = 30,
                 min_size: int = 256, max_size: int = 4096, amount: int = 42):
    for _ in range(amount):
        name_size = randint(min_name, max_name)
        ext = random_extension(extension)
        file_name = ''.join(sample(ascii_letters, name_size)) + '.' + ext
        if not os.path.exists(dir):
            os.mkdir(dir)
        file_name = os.path.join(dir, file_name)
        with open(file_name, 'ab') as file:
            size = randint(min_size, max_size)
            result = randbytes(size)
            file.write(result)


create_files(['txt', 'doc', 'md', 'rtf'], dir='test', amount=12)