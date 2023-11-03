# 4. Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в
# рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import random
import copy

def random_load_backpack(all_things: dict, backpack_capacity: int):
    # случайным образом наполняем пустой рюкзак вещами пока не останется выбора
    # или не будет заполнен полностью рюкзак
    #выбранные вещи, помещенные в рюкзак
    backpack_things = {}
    # оставшиеся вещи, для выбора
    remain_things = copy.deepcopy(all_things)
    # оставшаяся вместимость
    remain_capacity = backpack_capacity

    while remain_capacity > 0:
        # выбираем вещь случайным образом из оставшихся remain_things,
        # чтобы её вес был <= , чем оставшаяся вместимость remain_capacity
        remain_light_things = []  # список ключей оставшихся для выбора легких вещей
        for key, val in remain_things.items():
            if val <= remain_capacity:
                remain_light_things.append(key)

        #если легких вещей для выбора не осталось выходим из цикла, выбор завершён
        if len(remain_light_things) == 0:
            break

        # делаем случайный выбор легкой вещи
        new_thing_key = random.choice(remain_light_things)
        # добавляем вещь в рюкзак
        backpack_things[new_thing_key] = all_things[new_thing_key]
        # меняем значения оставшейся вместимости и оставшихся вещей для выбора
        remain_capacity -= backpack_things[new_thing_key]
        remain_things.pop(new_thing_key)  #удаляем из оставшихся вещей, вещь добавленную в рюкзак

    return backpack_things


if __name__ == "__main__":

    # полный перечень вещей для похода: ключ - название, значение - вес вещи (кг)
    all_things = {'куртка': 5, 'шапка': 3, 'штаны': 2, 'палатка': 15, 'компас': 2, 'кружка': 2, 'кастрюля': 5,
                  'поварежка': 3, 'крупа': 2, 'чай': 1, 'зажигалка': 1, 'аптечка': 3, 'ноутбук': 5}

    # вместимость рюкзака (кг)
    backpack_capacity = 16

    print('Варианты загрузки рюкзаков вещами.')
    for i in range(1, 6):
        print(f'Рюкзак №{i}')
        backpack_things = random_load_backpack(all_things, backpack_capacity)
        common_weight = 0
        for key, val in backpack_things.items():
            print(f'предмет: {key}, вес: {val}кг.')
            common_weight += val
        print(f'Вместимость рюкзака: {backpack_capacity}кг, вес набора {common_weight}кг.\n')