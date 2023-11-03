# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
import random

get_class = lambda x: globals()[x]


class Factory:
    def __init__(self, name: str, animal_class: str, count: int):
        # animal_class - тип животного, count - количество животных
        self.name = name
        self.animals = []
        # if animal_class in self.globals.items():
        # создаем список с объектами класса животного animal_class
        for i in range(count):
            self.animals.append(get_class(animal_class)(i+1))
        self.count = count
        # else:

    #            self.count = 0

    def print_animals(self):
        res_str = ''
        for animal in self.animals:
            res_str += f'{type(animal)}, name={animal.name}, id={animal.id_}\n'
        return res_str

    def showdata(self):
        return f'Данные фабрики: Название - {self.name}\n' + \
               f'Список животных:\n{self.print_animals()}' + \
               f'Кол-во животных: {self.count}'


class Animal:
    def __init__(self, id_: str = None, name: str = None, bread: str = 'unknown', age: int = 0):
        self.id_ = id_
        self.name = name
        self.bread = bread
        self.age = age

    def print_specific(self):
        return f'данные Animal'


class Dog(Animal):
    def __init__(self, id_: str = None, name: str = None, bread: str = 'unknown', commands: list[str] = 'unknown'):
        super().__init__(id_, name, bread)
        self.commands = commands

    def print_specific(self):
        return f'{self.commands}'


class Fish(Animal):
    def __init__(self, id_: str = None, name: str = None, bread: str = 'unknown', count_fins: int = 0):
        super().__init__(id_, name, bread)
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'


class Bird(Animal):
    def __init__(self, id_: str = None, name: str = None, bread: str = 'unknown', count_flights: int = 0):
        super().__init__(id_, name, bread)
        self.count_flights = count_flights

    def print_specific(self):
        return f'{self.count_flights}'


#Создаем 2 фабрики с разными типами животных и их количеством
factory1 = Factory('Черкизово', 'Bird', 10)
factory2 = Factory('им.50 лет Октября', 'Fish', 5)

# Присваиваем имена конкретным объектам фабрики (демонстрация доступа к свойствам)
factory1.animals[3].name = 'Chicki'
factory1.animals[-1].name = 'Lady Gaga'

#Вывод данных по фабрикам
print(factory1.showdata())
print(factory2.showdata())
