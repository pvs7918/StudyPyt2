# Задание
# Написать программу, которая скачивает изображения с заданных URL-адресов и
# сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле,
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы
# командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого
# изображения и общем времени выполнения программы.

# многопроцессорный подход

import os
import sys
import multiprocessing
import time

import requests

def download_image(url):
    # создать подкаталог для сайта
    print(f'Загрузка картинки: {url}')
    site_save_dir = 'img'
    # создаем если нет подкаталог img для изображений
    if not os.path.exists('img'):
        os.mkdir(site_save_dir)

    # замеряем время скачивания каждого файла в отдельности
    file_start = time.time()

    res = requests.get(url, stream=True)
    if res.status_code == 200:
        # определяем название файла на диске
        file_path = os.path.join(site_save_dir, url.split("/")[-1])
        # сохраняем файл
        try:
            with open(file_path, 'wb') as f:
                f.write(res.content)
                file_end = time.time()
                print(f'Файл: {file_path}, время скачивания: {file_end - file_start}')
        except:
            print(f'Ошибка при сохранении файла {file_path}')
    else:
        print(f'Ошибка загрузки картинки: {url}, код ошибки={res.status_code}')


if __name__ == "__main__":

    # 0-й параметр sys.argv - это название запускаемого модуля. его пропускаем
    # Параметры командной строки задаем в контекстном меню PyCharm. Пункт Modify Run Configuration...
    if len(sys.argv) == 1:
        img_urls = [
                       'https://c.rdrom.ru/touch/images/mobile/icons/apple-touch-icon.png',
                       'https://p2.piqsels.com/preview/23/378/471/bridge-california-cliff-golden-gate-bridge.jpg',
                       'https://p2.piqsels.com/preview/905/36/962/blue-sky-clouds-flying-hd-wallpaper.jpg',
                       'https://p2.piqsels.com/preview/718/374/435/animal-animal-photography-big-cat-blur.jpg',
                       'https://p2.piqsels.com/preview/262/885/283/birds-hd-wallpaper-ocean-sea.jpg',
                       'https://p2.piqsels.com/preview/530/180/30/aerial-bank-buildings-city.jpg',
                       'https://p2.piqsels.com/preview/837/595/710/aerial-architectural-design-architecture-buildings.jpg',
                       'https://p2.piqsels.com/preview/715/993/68/aerial-architecture-buildings-capital.jpg',
                       'https://p2.piqsels.com/preview/1024/853/225/animal-bird-colorful-colourful.jpg',
                       'https://p2.piqsels.com/preview/341/93/251/advent-background-board-brown.jpg'
                   ] * 10
    else:
        #если заданы параметры командной строки, то их используем как список с url-адресами картинок
        # URL в параметрах командной строки задаем без кавычек
        img_urls = sys.argv[1:]

    #выводим сфорфмированный список файлов
    for param in img_urls:
        print(param)

    # замеряем общее время работы программы
    start = time.time()

    processes = []

    for url in img_urls:
        p = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print(f'Общее время выполнения программы: {end - start}')
    print('Готово!')
