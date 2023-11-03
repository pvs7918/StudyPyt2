# Задание №7
# Напишите программу на Python, которая будет находить сумму элементов массива из
# 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

# используя threading

import random
import threading
import time

def summa(ints):
    global total_summa
    total_summa += sum(ints)

threads = []

arr = [random.randint(1, 101) for _ in range(1, 1000000)]

left = arr[:len(arr)//2]
right = arr[len(arr)//2+1:]

total_summa = 0

start = time.time()

t1 = threading.Thread(target=summa, args=(left, ))
t1.start()

t2 = threading.Thread(target=summa, args=(right, ))
t2.start()

t1.join()
t2.join()

end = time.time()

print(total_summa)
print(end - start)
print('Готово!')