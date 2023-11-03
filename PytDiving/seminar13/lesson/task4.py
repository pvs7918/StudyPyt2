# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import random
import json


class User():

    def __init__(self, name="", id=0, access_lvl=0):
        self.name = name
        self.id = id
        self.access_lvl = access_lvl
        self.users_list = []  # список пользователей

    def user_input(self):
        user_list = []  # Данные одного пользователя
        users_list = []  # список пользователей

        while True:
            try:
                name = input('Name: ')
                if not str.istitle(name):
                    raise ValueError
            except Exception as e:
                print(e)
            if not name:
                for i in user_list:
                    users_list.append(User(*i))
                self.users_list = users_list
                break
            while True:
                user_id = random.randint(10_000, 100_000)
                if user_id not in [uid[2] for uid in user_list]:
                    break
            while True:
                lvl = input('lvl: ')
                if lvl.isdigit() and 0 < int(lvl) < 8:
                    user_list.append((name, int(user_id), int(lvl)))
                    break

    def __str__(self):
        return f'{self.name} {self.id} {self.access_lvl}'

    def json_write(self, file_name):
        result_dict = {}

        for user in self.users_list:
            result_dict[user.id] = [user.name, user.access_lvl]
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(result_dict, f, indent=4, ensure_ascii=False)
        except EOFError as e:
            print(e)

    def json_read(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
        except EOFError as e:
            print(e)

        # for key in new_dict:
        #     self.users_list.append(User(new_dict[key][0], key, new_dict[key][1]))


new_user = User('', '', '')
new_user_list = new_user.user_input()
new_user.json_write('task4.json')

new_user.json_read('task4.json')
for i in new_user.users_list:
    print(i)
