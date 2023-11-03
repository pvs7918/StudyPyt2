# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

import random

things = ['рюкзак', 'лопатка', 'палатка', 'компас', 'кружка', 'кастрюля',
          'поварежка', 'крупа', 'чай', 'зажигалка']

friends = ['Миша', 'Костя', 'Славик']

one_friend_things_count = 4  # Количество вещей у одного друга

#формируем словарь вещей которые взяли друзья


friend_fings = {}
for fr in friends:
    # методом выбираем случайным образом нужное количество вещей из списка,
    # значения не повторяются у одного человека
    friend_fings[fr] = set(random.sample(things, one_friend_things_count))

# Показать список сформированный друзей вещей
print(f'\nСформированный список друзей с вещами:\n {friend_fings}')

# Ответы на вопросы:
# Какие вещи взяли все три друга
#множество взятых вещей
taken_things = set()
for cur_things in friend_fings.values():
    for val in cur_things:
        taken_things.add(val)
print(f'\nобщий список вещей друзей:\n {taken_things}')


# Какие вещи взяли все три друга
all_things_list_of_sets = []
for cur_things in friend_fings.values():
    all_things_list_of_sets.append(cur_things)
#находим пересечение списка множеств
common_things = set.intersection(*all_things_list_of_sets)
print(f'\nКакие вещи взяли все три друга:\n {common_things}\n')


#Показать уникальные вещи, которых нет у других
for fr1_key, fr1_val in friend_fings.items():
    for fr2_key, fr2_val in friend_fings.items():
        #множество вещей других друзей
        other_friends_things_list = set()
        if fr1_key != fr2_key:
            other_friends_things_list = other_friends_things_list.union(fr2_val)

    cur_friend_unic_things = fr1_val.difference(other_friends_things_list)
    print(f'У {fr1_key}:\nуникальные вещи: {cur_friend_unic_things},')

    cur_friend_absent_things = other_friends_things_list.difference(fr1_val)
    print(f'нет вещей, которые есть у всех остальных: {cur_friend_absent_things}.\n')