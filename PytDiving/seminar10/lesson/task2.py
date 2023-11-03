# Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Square:
    def __init__(self, length, width=None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def square(self):
        return self.length * self.width

    def perimetr(self):
        return 2 * (self.length + self.width)


sq1 = Square(5)
print(f'{sq1.length=}, {sq1.width=}, {sq1.square()=}, {sq1.perimetr()=}')
