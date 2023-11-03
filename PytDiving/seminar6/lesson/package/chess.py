# 2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
# напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.
import random


def desk_check_beating(position: list) -> (bool, str):
    # функция проверяет позицию из 8 ферзей
    # position - расположение ферзей на доске проверяем бьют они друг друга или нет
    # например [1, 5, 8, 6, 3, 7, 2, 4]
    # возвращается кортеж - bool (False - не бюьт друг друга, True - бьют),
    # str - пояснение какая фигура какую бьёт

    # заполняем доску нулями для начала
    desk = [[0 for i in range(8)] for i in range(8)]
    # расставляем ферзей = 1 - ячейка занята ферзём
    for i, pos in enumerate(position):
        desk[pos - 1][i] = 1
        # делаем сразу проверку бьют ли ферзи друг друга по горизонтали
        for j in range(i):
            if position[i] == position[j]:
                return True, f'Ферзь ({position[i] + 1},{i + 1}) бьет ферзя ({position[j] + 1},{j + 1})'

    # проверку по вертикали не делаем так как каждый ферзь в своей колонке согласно позиции
    # проверки по диагонали
    for i, pos in enumerate(position):  # для каждого ферзя (она же колонка)
        # позиция i-го ферзя на доске
        br = pos - 1
        bc = i

        # проверка бития вверх-налево
        r = br - 1
        c = bc - 1
        r, c = beating(desk, r, c, -1, -1, 0, 0)
        if r > 0 and c > 0:
            return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'

        # проверка бития вверх - направо
        r = br - 1
        c = bc + 1
        r, c = beating(desk, r, c, -1, 1, 0, 7)
        if r > 0 and c > 0:
            return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'

        # проверка бития вниз - налево
        r = br + 1
        c = bc - 1
        r, c = beating(desk, r, c, 1, -1, 7, 0)
        if r > 0 and c > 0:
            return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'

        # проверка бития вниз - направо
        r = br + 1
        c = bc + 1
        r, c = beating(desk, r, c, 1, 1, 7, 7)
        if r > 0 and c > 0:
            return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'

    return False, 'Ферзи не бьют друг друга'  # False


def beating(desk, r, c, r_step, c_step, r_max, c_max) -> (int, int):
    # для упрощения кода, повторящийся код вынес в отдельную функцию
    while r * r_step <= r_max and c * c_step <= c_max:
        if desk[r][c] == 1:
            return r, c
        r += r_step
        c += c_step

    return -1, -1


def desk_check_beating_old(position: list) -> (bool, str):
    # функция проверяет позицию из 8 ферзей
    # position - расположение ферзей на доске проверяем бьют они друг друга или нет
    # например [1, 5, 8, 6, 3, 7, 2, 4]
    # возвращается кортеж - bool (False - не бюьт друг друга, True - бьют),
    # str - пояснение какая фигура какую бьёт

    # заполняем доску нулями для начала
    desk = [[0 for i in range(8)] for i in range(8)]
    # расставляем ферзей = 1 - ячейка занята ферзём
    for i, pos in enumerate(position):
        desk[pos - 1][i] = 1
        # делаем сразу проверку бьют ли ферзи друг друга по горизонтали
        for j in range(i):
            if position[i] == position[j]:
                return True, f'Ферзь ({position[i] + 1},{i + 1}) бьет ферзя ({position[j] + 1},{j + 1})'

    # проверки - бьют друг друга или нет
    # проверку по вертикали не делаем так как каждый ферзь в своей колонке согласно позиции
    # проверка по диагонали
    for i, pos in enumerate(position):  # для каждого ферзя (она же колонка)
        # позиция i-го ферзя на доске
        br = pos - 1
        bc = i

        # проверки по диагонали
        # вверх-налево
        r = br - 1
        c = bc - 1

        while r >= 0 and c >= 0:
            if desk[r][c] == 1:
                return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'
            r -= 1
            c -= 1

        # вверх - направо
        r = br - 1
        c = bc + 1

        while r >= 0 and c < 8:
            if desk[r][c] == 1:
                return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'
            r -= 1
            c += 1

        # вниз - налево
        r = br + 1
        c = bc - 1
        while r < 8 and c >= 0:
            if desk[r][c] == 1:
                return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'
            r += 1
            c -= 1

        # вниз - направо
        r = br + 1
        c = bc + 1
        while r < 8 and c < 8:
            if desk[r][c] == 1:
                return True, f'Ферзь ({br + 1},{bc + 1}) бьет ферзя ({r + 1},{c + 1})'
            r += 1
            c += 1

    return False, 'Ферзи не бьют друг друга'  # False


def print_position(position: list):
    # вывод на экран позиции

    print(f'Позиция: {position}')
    # заполняем доску нулями для начала
    desk = [[0 for i in range(8)] for i in range(8)]
    # расставляем ферзей = 1 - ячейка занята ферзём
    for i, pos in enumerate(position):
        desk[pos - 1][i] = 1
    # печать строк
    for i in range(len(position)):
        print(desk[i])


def generate_random_position() -> list:
    # функция возвращает случайным образом сгенерированную позицию
    # для меньшего количества брака каждая последующая позиция
    # исключает уже выбранные в pos номера. Так быстрее подбираем вариант
    pos = []
    for i in range(8):
        cur_pos = 0
        while cur_pos == 0:
            cur_pos = random.randint(1, 8)
            if cur_pos in pos:
                cur_pos = 0
            else:
                pos.append(cur_pos)  # если такой позиции ещё не было то добавляем
    return pos


if __name__ == '__main__':
    # тестирование
    position = [1, 5, 8, 6, 3, 7, 2, 4]  #позиция когда не бьют друг друга
    #position = [5, 7, 8, 6, 3, 1, 2, 4]  # позиция когда бьют друг друга
    print_position(position)
    status, reason = desk_check_beating(position)
    print(reason)
