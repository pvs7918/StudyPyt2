# 📌Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌При нового экземпляра класса, старые данные из ранее созданных экземпляров
# сохраняются в пару списковархивов
# 📌list-архивы также являются свойствами экземпляра

class Archive:
    """Строка документации для класса Архив, которая хранит пару свойств,
            а также Архив предыдущих значений"""

    _instance = None
    _archive = []

    def __new__(cls, name: str, age: int):
        instance = super().__new__(cls)
        if cls._instance:
            cls._archive.append(cls._instance)
        cls._instance = instance
        instance.archive = cls._archive.copy()
        return cls._instance

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        """дандер-метод __repr__ - печать объекта Archive"""
        return f'{self.name} {self.age}'

def main():
    player1 = Archive('STONE', 39)
    player2 = Archive('Karina', 18)
    player3 = Archive('Misha', 25)
    player4 = Archive('Dima', 38)
    print(player1)
    print(player1.archive)
    print(player2)
    print(player2.archive)
    print(player3)
    print(player3.archive)
    print(player4)
    print(player4.archive)

    # Вывод документации
    print('Документация класса MyString')
    print(Archive.__doc__)
    print('Документация объекта класса MyString')
    print(player1.__doc__)
    print('Документация метода объекта __new__ класса MyString')
    print(player1.__repr__.__doc__)

if __name__ == '__main__':
    main()