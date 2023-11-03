# 3. Напишите функцию в шахматный модуль. Используйте генератор случайных
#  чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный
#  случайные варианты и выведите 4 успешных расстановки.


from package import print_position, desk_check_beating, generate_random_position

number_true_pos = 4
cur_true_pos = 0
print('Список верных позиций:\n')

while cur_true_pos < number_true_pos:
    position = generate_random_position()
    status, reason = desk_check_beating(position)
    if not status:  # False - ферзи не бьют друг друга
        print_position(position)
        cur_true_pos += 1