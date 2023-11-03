# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и
# выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input('N: '))
ls = []
summary = 0

for i in range(n):
    k = i + 1
    ls.append(int(round(((1 + 1 / k) ** k))))
    summary += ls[i]

print(f'Для n = {n}: {ls} -> {summary}')
