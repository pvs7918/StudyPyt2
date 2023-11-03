# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).

# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

import random
import json

def user_input():
    user_list = []
    while True:
        name = input("Name: ")
        if not name:
            return user_list
        while True:
            user_id = random.randint(10000, 100000)
            if user_id not in [uid[2] for uid in user_list]:
                break
        while True:
            lvl = input("lvl: ")
            if lvl.isdigit() and 0 < int(lvl) < 8:
                user_list.append((name, lvl, user_id))
                break

def json_write():
    user_list = user_input()
    result_dict = {}

    for user in user_list:
        if user[1] in result_dict:
            result_dict[user[1]].update({user[2]:user[0]})
        else:
            result_dict[user[1]] = {user[2]:user[0]}

    with open('task2_result.json','w',encoding='utf-8') as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)

json_write()