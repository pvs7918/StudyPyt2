# Задание №7
# Напишите программу на Python, которая будет находить сумму элементов массива из
# 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

# используя multiprocessing

import random
import asyncio
import time

async def summa(ints):
    global total_summa
    total_summa += sum(ints)

async def main():
    t1 = asyncio.create_task(summa(left))
    t2 = asyncio.create_task(summa(right))
    await t1
    await t2


# if __name__ == '__main__':

arr = [random.randint(1, 101) for _ in range(1, 1000000)]

left = arr[:len(arr) // 2]
right = arr[len(arr) // 2 + 1:]

total_summa = 0

start = time.time()
asyncio.run(main())
print(total_summa)
end = time.time()

print(end - start)
print('Готово!')
