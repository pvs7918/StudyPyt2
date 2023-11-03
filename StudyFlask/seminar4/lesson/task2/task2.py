# Задание №2
# Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса.
# после загрузки данных нужно записать их в отдельные файлы.
# используйте процессы.

# Задание №1
# Написать программу, которая считывает список из 10 URL-адресов и
# одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.

import multiprocessing
import time
import requests

urls = [
    'https://python.org',
    'https://mail.ru',
    'https://practicum.yandex.ru',
    'https://gb.ru/geek_university/developer/programmer/python',
    'https://netology.ru/programs/python',
    'https://synergyacademy.com/program/python-razrabotchik',
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://tproger.ru/articles/podrobnoe-opisanie-jazyka-python-dlja-nachinajushhih',
    'https://github.com/python',
    'https://habr.com/ru/articles/450474/'
]

def download(url, i):
    response = requests.get(url)
    filename = f'site_{i}.html'

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)


if __name__ == '__main__':
    processes = []

    start = time.time()

    for index, url in enumerate(urls):
        p = multiprocessing.Process(target=download, args=(url, index))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print(end - start)
    print('Готово!')