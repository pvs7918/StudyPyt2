# 📌 Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Animal:
    def __init__(self, name:str = None, bread:str = 'unknown', age: int = 0):
        self.name = name
        self.bread = bread
        self.age = age

    def print_specific(self):
        return f'данные Animal'

class Dog(Animal):
    def __init__(self, name: str = None, bread: str = 'unknown', commands: list[str]='unknown'):
        super().__init__(name,bread)
        self.commands = commands

    def print_specific(self):
        return f'{self.commands}'

class Fish(Animal):
    def __init__(self, name: str = None, bread: str = 'unknown', count_fins: int = 0):
        super().__init__(name, bread)
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'

class Bird(Animal):
    def __init__(self, name: str = None, bread: str = 'unknown', count_flights: int = 0):
        super().__init__(name, bread)
        self.count_flights = count_flights

    def print_specific(self):
        return f'{self.count_flights}'



animal = Animal('Leha', 'Cat', 12)
dog = Dog('Boy', 'Husky', ['Голос', 'Сидеть!'])
fish = Fish('Nemo', 'Gold Fish', 3)
bird = Bird('Kesha', 'Попугай', 2)

print(animal.print_specific())
print(dog.print_specific())
print(fish.print_specific())
print(bird.print_specific())
