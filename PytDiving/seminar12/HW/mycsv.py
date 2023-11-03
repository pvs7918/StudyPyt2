import csv


def read_csv(file_name) -> dict:
    subjs = {}
    with open(file_name, 'r', newline='') as f:
        csv_file = csv.reader(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        for i, line in enumerate(csv_file):
            if i!= 0:
                subjs[line[0]] = line[1]
    return subjs


# Запись csv
def write_csv(file_name: str, subjs: dict):
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write,
                                   fieldnames=["name", "abr"],
                                   dialect='excel',
                                   quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        dict_row = {}
        for key, val in subjs.items():
            dict_row["name"] = key
            dict_row["abr"] = val
            csv_write.writerow(dict_row)


if __name__ == "__main__":
    subjects = {'Математика': 'mat', 'Русский язык': 'rus', 'Литература': 'lit', 'История': 'his',
                'Английский язык': 'eng', 'Физика': 'fiz', 'Химия': 'che'}

    # write_csv('subjects.csv', subjects)
    subres = read_csv('subjects.csv')
    print(subres)