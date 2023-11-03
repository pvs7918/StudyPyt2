# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius**2

c1 = Circle(20)
print(f'{c1.radius=}, {c1.length()=}, {c1.square()=}')