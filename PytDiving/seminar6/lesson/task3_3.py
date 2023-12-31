# Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.

# Отдельно напишите функцию, которая выводит результаты угадывания из
# защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

def zagadka(sagadka: str, answers: list, count_: int = 5):
    print(f'Загадка - {sagadka}')
    try_ = 1

    while count_:
        user_ansver = input('Ваш ответ: ').lower()

        if user_ansver in answers:
            return try_

        try_ += 1
        count_ -= 1

    return 0


def puzzle():
    puzzles = {'Зимой и летом одним цветом?': ['елка', 'ёлка', 'ель'],
               'Висит груша - нельзя скушать': ['лампочка', 'лампа'],
               'Не лает не кусает - в дом не пускает': ['замок', 'замочек']
               }

    for key, value in puzzles.items():
        fun_2(key, zagadka(key, value))

    print(_result_dict)


# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.

# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в
# удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

_result_dict = {}


def fun_2(zagad: str, number: int = 0):
    _result_dict[zagad] = number

# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на
# угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# см. модуль secret_.py
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
# (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в
# удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


from secret_ import zagadka as zag, puzzle

# print(zag('Зимой и летом одним цветом?', ['елка', 'ёлка', 'ель'], 5))
puzzle()