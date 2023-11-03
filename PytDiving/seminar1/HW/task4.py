# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за
# 10 попыток. # Программа должна подсказывать «больше» или «меньше» после каждой попытки.

# вариант - загадывает компьютер, отгадывает пользователь
import random

# загаданное число
up_value = 100000
hidden_number = random.randint(0, up_value)
attemp_cnt = 10
cur_attemp = 1  # номер попытки отгадывания

while cur_attemp <= attemp_cnt:
    variant = int(input(f'Отгадайте загаданное число (от 0 до {up_value}). Попытка {cur_attemp}: '))
    if variant < 0 or variant > up_value:
        print('Введенное число выходит за рамки условий')
    elif variant >= 0 and variant <= up_value:
        if variant == hidden_number:
            print('Вы отгадали число! Поздравляю!')
            break
        elif variant < hidden_number:
            print('Заданное число больше!')
        elif variant > hidden_number:
            print('Заданное число меньше!')
    cur_attemp += 1

if cur_attemp > attemp_cnt and variant != hidden_number:
    print(f'Вы исчерпали 10 попыток и не отгадали число! Увы! Загаданное число - {hidden_number}')
