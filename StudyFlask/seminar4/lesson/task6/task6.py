# Задание №4
# Создать программу, которая будет производить подсчет количества слов в
# каждом файле в указанной директории и выводить результаты в консоль.
# Используйте потоки.
import os
import asyncio

import aiofiles as aiofiles
import aiohttp
import time

async def word_counter(file_path):
    # вариант 1 - with open (он блокирует доступ к файлу)
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     text = file.read()
    #вариант 2 - async with aiofiles.open (нужен при одновременном доступе нескольких пользователей к файлу)
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as file:
        text = await file.read()
        words_count = len(text.split(' '))
        print(f'файл - {file_path}, слов-{words_count}')

async def main():
    tasks = []

    for root, dirs, files in os.walk('htmls'):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            tasks.append(asyncio.create_task(word_counter(file_path)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    end = time.time()

    print(end - start)
    print('Готово')
