def get_secret(secret_text: str, answers: list, max_count: int):
    print(f'Отгадайте загадку - {secret_text}')
    try_ = 1
    while try_ <= max_count:
        user_answer = input('Ваш ответ: ').lower()

        if user_answer in answers:
            print(f'Отгадали! Количество попыток - {try_}')
            return try_
        try_ += 1
    print('Жаль, не смогли отгадать ((')
    return 0

def guess_puzzles(puzl_dict: dict):
    for k, val in puzl_dict.items():
        get_secret(k, val, 2)


# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


def zagadka(zagadka_text: str, answers: list, max_count: int = 5):
    print(f'Загадка - {zagadka_text}')
    try_ = 1
    while try_ <= max_count:
        user_answer = input('Ваш ответ: ').lower()

        if user_answer in answers:
            print(f'Отгадали! Количество попыток - {try_}')
            return try_
        try_ += 1
    print('Жаль, не смогли отгадать ((')
    return 0

def puzzle():
    puzzles = {'Зимой и летом одним цветом': ['елка','ёлка','ель'],
               'Висит груша - нельзя скушать': ['лампочка','лампа'],
               'Не лает н кусает - в дом не пускает': ['замок','замочек']
                }
    for key, value in puzzles.items():
        fun_2(key,zagadka(key,value))

    print(_result_dict)


_result_dict = {}
def fun_2(zagad: str, number: int = 0):
    _result_dict[zagad] = number