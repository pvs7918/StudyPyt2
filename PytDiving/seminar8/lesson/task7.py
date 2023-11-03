# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

import csv
import pickle

with open("task5_json.csv", "r", newline="") as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        line = pickle.dumps(line)
        print(line)
        print()

