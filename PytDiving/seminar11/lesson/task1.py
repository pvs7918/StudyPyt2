# 📌Создайте класс Моя Строка, где:
# 📌будут доступны все возможности str
# 📌дополнительно хранятся имя автора строки и время создания (time.time)
import datetime


class MyString(str):
    """Расширенная строка, которая имеет допонлительные свойства name, date - дата создания"""
    def __new__(cls, value, name):
        """дандер-метод __new__ класса MyString"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance

first_string = MyString('abc','author')
print(first_string)
print(first_string.name)
print(first_string.date)

# Вывод документации по классу и его методам
print('Документация класса MyString')
help(MyString)
print('Документация объекта класса MyString')
help(first_string)

print('Документация класса MyString')
print(MyString.__doc__)
print('Документация объекта класса MyString')
print(first_string.__doc__)
print('Документация метода объекта __new__ класса MyString')
print(first_string.__new__.__doc__)
