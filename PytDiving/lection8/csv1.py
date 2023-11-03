# При работе с CSV необходимо указывать параметр newline=’’ во время открытия файла.
# import csv
# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
#     print(type(line))




# Добавим несколько параметров для чтения csv с разделителем Tab
# import csv
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(line)
#     print(type(line))


# Запись csv
# with (
# open('biostats_tab.csv', 'r', newline='') as f_read,
# open('new_biostats.csv', 'w', newline='', encoding='utf-8')
# as f_write
# ):
#     csv_read = csv.reader(f_read, dialect='excel-tab',
#         quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel',
#                            delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     all_data = []
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line)
#         else:
#             line[2] += 1
#             for j in range(2, 4 + 1):
#                 line[j] = int(line[j])
#             all_data.append(line)
#     csv_write.writerows(all_data)



# Чтение - запись в CSV в словарь
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex",
#         "age", "height", "weight", "office"],
#         restkey="new", restval="Main Office",
#         dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     # csv.QUOTE_NONNUMERIC указывает объектам записи указывать все не числовые поля.
#     # Так же csv.QUOTE_NONNUMERIC указывает объекту чтения преобразовать
#     # все поля без кавычек в тип float.
#     # csv.excel_tab — диалект CSV - файла, обычно генерируемого программой Excel
#     # с настройкой "разделитель с помощью TAB".
#
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')


# Запись словаря в CSV-файл
# Для записи содержимого словаря в CSV используют класс DictWriter. Его параметры
# схожи с рассмотренными выше параметрами DictReader.
# import csv
# from typing import Iterator
# with (
# open('biostats_tab.csv', 'r', newline='') as f_read,
# open('biostats_new.csv', 'w', newline='', encoding='utf-8')
# as f_write
# ):
#     csv_read: Iterator[dict] = csv.DictReader(f_read,
#         fieldnames=["name", "sex", "age", "height", "weight", "office"],
#         restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.DictWriter(f_write, fieldnames=["id", "name",
#         "office", "sex", "age", "height", "weight"], dialect='excel-tab',
#         quoting=csv.QUOTE_ALL)
#     csv_write.writeheader()
#     all_data = []
#     for i, dict_row in enumerate(csv_read):
#         if i != 0:
#             dict_row['id'] = i
#             dict_row['age'] += 1
#     all_data.append(dict_row)
#     csv_write.writerows(all_data)


# пример
import csv
with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, fieldnames=["number",
        "name", "data"], restval='Hello world!', dialect='excel',
        delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row['number'] = i
        dict_row['name'] = str(i)
        csv_write.writerow(dict_row)