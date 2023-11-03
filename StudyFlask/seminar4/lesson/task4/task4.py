# Задание №4
# Создать программу, которая будет производить подсчет количества слов в
# каждом файле в указанной директории и выводить результаты в консоль.
# Используйте потоки.
import os
import threading
import time

def word_counter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words_count = len(text.split(' '))
        print(f'файл - {file_path}, слов-{words_count}')


if __name__ == '__main__':
    threads = []

    start = time.time()

    for root, dirs, files in os.walk('htmls'):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            t = threading.Thread(target=word_counter, args=(file_path, ))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    end = time.time()

    print(end - start)
    print('Готово')
