# Задание №7
# Напишите программу на Python, которая будет находить сумму элементов массива из
# 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

# используя multiprocessing

import random
import multiprocessing
import time

def summa(ints, total_summa):
    with total_summa.get_lock():
        total_summa.value += sum(ints)

threads = []

arr = [random.randint(1, 101) for _ in range(1, 1000000)]

left = arr[:len(arr)//2]
right = arr[len(arr)//2+1:]

total_summa = multiprocessing.Value('i', 0)

start = time.time()

def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock():
            cnt.value += 1
        print(f"Значение счетчика: {cnt.value:_}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=summa, args=(left, total_summa))
    p1.start()
    p2 = multiprocessing.Process(target=summa, args=(right, total_summa))
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(total_summa)
    print(end - start)
    print('Готово!')
