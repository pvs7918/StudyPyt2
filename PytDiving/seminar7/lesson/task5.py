# ✔Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры: ✔расширение
# ✔минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔количество файлов, по умолчанию 42
# ✔Имя файла и его размер должны быть в рамках переданного диапазона.

import random
from random import randint, randbytes, sample, choice
from string import ascii_letters
import os


def random_extension(list_ext: list[str]) -> str:
    return random.choice(list_ext)


def create_files(extension: list[str], min_name: int = 6, max_name: int = 30,
                 min_size: int = 256, max_size: int = 4096, amount: int = 42):
    for _ in range(amount):
        name_size = randint(min_name, max_name)
        ext = random_extension(extension)
        file_name = ''.join(sample(ascii_letters, name_size)) + '.' + ext
        file_name = os.path.join('data', file_name)
        with open(file_name, 'ab') as file:
            size = randint(min_size, max_size)
            result = randbytes(size)
            file.write(result)


create_files(['txt', 'doc', 'md', 'rtf'], amount=12)