# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle
import os

nes_extension = "json"

def json_to_pickle(path):
    for file in (os.listdir()):
        if os.path.isfile(file):
            initial_name, initial_ext = os.path.join(file).split(".")
            if initial_ext == nes_extension:
                with open(file, 'r', encoding='utf-8') as file:
                    new_dict = json.load(file)
                    initial_name = initial_name + '.pickle'
                    with open(initial_name, "wb") as file:
                        pickle.dump(new_dict, file)

json_to_pickle(os.path.join(os.getcwd()))