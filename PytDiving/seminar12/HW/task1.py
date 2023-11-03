# 2.	Создайте класс студента.
# 3.	Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# 4.	Названия предметов должны загружаться из файла CSV при создании экземпляра.
#       Другие предметы в экземпляре недопустимы.
# 5.	Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# 6.	Также экземпляр должен сообщать средний балл по тестам для каждого предмета
#       и по оценкам всех предметов вместе взятых.

import random
import mycsv


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Text:
    def __init__(self, param=''):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с большой буквы.')
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы.')


class Student:
    # ФИО студента
    fullname: Text()  # с помощью класса-дескриптора Text определяем допуски - начинается с заглавной буквы и только буквы
    # оценки по предметам (от 2 до 5)
    subjs_marks = dict
    # баллы по тестам по предметам (от 0 до 100)
    tests_score = dict

    # словарь средних баллов по тестам для каждого предмета
    _tests_avg_score_dict: dict
    # средний балл по оценкам всех предметов вместе взятых
    _subjs_avg_mark: float

    def __init__(self, fullname: Text(), subjs_marks: dict, tests_score: dict):
        # ФИО студента
        self.fullname = fullname
        # словарь оценок по предметам
        self.subjs_marks = subjs_marks
        # словарь баллов по тестам
        self.tests_score = tests_score

    def __str__(self):
        res_text = f'Студент: {self.fullname}\nОценки по предметам: {self.subjs_marks}.\n' \
                   f'Баллы по тестам: {self.tests_score}.\n{self.avg}'
        return res_text

    # через свойство avg вычисляем и получаем средние баллы по тестам предметов и общий средний балл
    @property
    def avg(self):
        self._tests_avg_score_dict = {}
        # метод считает средний балл тестов по каждому предмету
        # и общую средний оценку по всем предметам

        # общая средняя оценка по предметам
        summ = 0
        cnt = 0
        for cur_mark in self.subjs_marks.values():
            summ += cur_mark[0]
            cnt += 1
        res_text = f'Общая средняя оценка по предметам: {summ / cnt:.1f}\n'

        summ = 0
        cnt = 0
        for cur_score in self.tests_score.values():
            summ += cur_score[0]
            cnt += 1
            # средние баллы по тестам хранятся в виде суммы балов по предмету и количества отметок
            avg_score, avg_cnt = self._tests_avg_score_dict.get(cur_score[1], (0, 0))
            self._tests_avg_score_dict[cur_score[1]] = (avg_score + cur_score[0], avg_cnt + 1)

        res_text += f'Средние баллы по предметам:\n'

        for key, val in self._tests_avg_score_dict.items():
            res_text += f'предмет: {key} - средний балл: {val[0] / val[1]:.1f}\n'

        return res_text


if __name__ == "__main__":
    # читаем перечень предметов из файла CSV согласно задания
    subjects = mycsv.read_csv('subjects.csv')

    # список имен студентов
    student_names = ["Иванов Иван", "Сидоров Петр", "Петрова Мария"]

    subjects_eng_name_list = list(subjects.values())
    # формируем stud_list список объектов класса Student, отметки по тестам заполняем случайным образом
    stud_list = []
    for name in student_names:
        # формируем словарь оценок по предметам студента
        str1: Text() = name
        subjs_marks: dict[int, tuple[Range(2, 5), str]] = {}
        # с помощью sample берем случайную выборку половины предметов
        for i, val in enumerate(random.sample(subjects_eng_name_list, len(subjects_eng_name_list) // 2)):
            subjs_marks[i + 1] = (random.randint(2, 5), val)
        # формируем словарь баллов по тестам студента
        tests_score: dict[int, tuple[Range(0, 100), str]] = {}
        for i in range(1, random.randint(6, 11)):
            tests_score[i] = (random.randint(0, 100), random.choice(subjects_eng_name_list))
        # добавляем сформированную запись о студенте в список студентов
        stud_list.append(Student(name, subjs_marks, tests_score))
        # выводим данные текущего студента. Общие отметки выводятся через свойство avg в методе __str__
        print(stud_list[-1])
