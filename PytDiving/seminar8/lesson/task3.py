# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import random
import csv


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


def csv_write():
    user_list = user_input()
    result_dict = {}

    for user in user_list:
        if user[1] in result_dict:
            result_dict[user[1]].update({user[2]: user[0]})
        else:
            result_dict[user[1]] = {user[2]: user[0]}

    with open('task3_result.csv', 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.DictWriter(f,
                                   fieldnames=["name", "access level", "id"],
                                   dialect='excel',
                                   quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        dict_row = {}
        for row in user_list:
            dict_row["name"] = row[0]
            dict_row["access level"] = row[1]
            dict_row["id"] = int(row[2])
            csv_write.writerow(dict_row)


csv_write()
