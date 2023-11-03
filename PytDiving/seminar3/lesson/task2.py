# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

import random

my_list = []
for i in range(21):
    my_list.append(random.randint(0, 10))

user_input = input()

if user_input.isdigit():
    print("Целое число ", user_input)

elif user_input.replace(".","").replace("-","").isdigit():
    print("Вещественное число ", user_input)

elif user_input == user_input.lower():
    print("Все строчные: ", user_input)
else:
    print("Есть хотя бы одна заглавная: ", user_input.upper())