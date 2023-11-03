# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п.
# на ваш выбор.
# 📌У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.

class Person:

    def __init__(self, first_name, second_name, last_name, phone, age):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.phone = phone
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'

    def person_age(self):
        return self._age

p1 = Person('Илья', 'Петрович', 'Сидоров', 345345345, 32)
print(p1.person_age())
p1.birthday()
print(p1.person_age())
print(p1.full_name())


