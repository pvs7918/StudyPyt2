# 1.
# б. Написать программу, которая выводит в консоль таблицу умножения "как на тетрадках"
rows = 10
cols = 5

print('Таблица умножения:')

for i in range(2, rows + 1):
    tmp_str = ''
    for j in range(2, cols + 1):
        tmp_str += f'{i:2} *{j:2} ={i * j:2}'  # :2 - количество знаков для вывода параметра
        if j < cols + 1:
            tmp_str += (' ' * 4)
        else:
            tmp_str += '\n'
    print(tmp_str)
print()

cols = 9
for i in range(2, rows + 1):
    tmp_str = ''
    for j in range(6, cols + 1):
        tmp_str += f'{j:2} *{i:2} ={i * j:2}'  # :2 - количество знаков для вывода параметра
        if j < cols + 1:
            tmp_str += (' ' * 4)
        else:
            tmp_str += '\n'
    print(tmp_str)

