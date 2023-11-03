# Задание №4
# Создать программу, которая будет производить подсчет количества слов в
# каждом файле в указанной директории и выводить результаты в консоль.
# Используйте потоки.
import os
import multiprocessing
import time

def word_counter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words_count = len(text.split(' '))
        print(f'файл - {file_path}, слов-{words_count}')


if __name__ == '__main__':
    processes = []

    start = time.time()

    for root, dirs, files in os.walk('htmls'):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            p = multiprocessing.Process(target=word_counter, args=(file_path, ))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()

    end = time.time()

    print(end - start)
    print('Готово')
