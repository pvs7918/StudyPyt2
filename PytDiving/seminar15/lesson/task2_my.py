# 📌 На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import json
import os
import logging
from typing import Callable


def logging_outer(file_name) -> Callable:
    def inner_func(func):
        def wrapper(*args, **kwargs):
            my_dict = {func(*args, **kwargs): [arg for arg in args] + [(key, value) for key, value in kwargs.items()]}

            with logging.basicConfig(filename=file_name, filemode='w',
                                encoding='utf-8', level=logging.INFO) фы
            logging.warning(my_dict)
            return func(*args, **kwargs)
        return wrapper
    return inner_func


def outer(file_name) -> Callable:
    def inner_func(func):
        def wrapper(*args, **kwargs):
            my_dict = {func(*args, **kwargs): [arg for arg in args] + [(key, value) for key, value in kwargs.items()]}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            return func(*args, **kwargs)
        return wrapper
    return inner_func


@logging_outer('task2.log')
def function_json(*args, **kwargs) -> str:
    list_for_args = []
    list_kwargs = []
    if args:
        for i in args:
            list_for_args.append(i)
    if kwargs:
        for key, value in kwargs.items():
            list_kwargs.append(f'{key}={value}')
    result_str = ' '.join(list(map(str, list_for_args))) + ' '.join(list(map(str, list_kwargs)))

    return result_str