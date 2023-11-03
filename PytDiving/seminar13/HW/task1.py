# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # обновляем свойства треугольника
        self._set_properties()

    def _set_properties(self):
        """ делаем проверки допустимости  существования
            и устнавливаем свойства треугольника"""
        if self.a < 0:
            raise ErrorTriangleNegativeSide(self)

        if self.a > self.b + self.c:
            print('Сторона a больше суммы b и c!')
            raise ErrorTriangleNotExist(self)
        elif self.b > self.a + self.c:
            print('Сторона b больше суммы a и c!')
            raise ErrorTriangleNotExist(self)
        elif self.c > self.a + self.b:
            print('Сторона c больше суммы a и b!')
            raise ErrorTriangleNotExist(self)
        else:
            # это треугольник. Делаем доп.проверки его сторон
            self.equal_all_sides = False
            self.equal_two_sides = False

            if self.a == self.b and self.b == self.c:
                self.equal_all_sides = True
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                self.equal_two_sides = True

    def __str__(self):
        res = f'Треугольник со сторонами: a={self.a}, b={self.b}, c={self.c},\n'
        if self.equal_all_sides == True:
            res += 'Это равносторонний треугольник.'
        elif self.equal_two_sides == True:
            res += 'Это равнобедренный треугольник.'
        else:
            res += 'Это разносторонний треугольник.'
        return res + '\n'

    def __repr__(self):
        return f'a={self.a}, b={self.b}, c={self.c}'


class ErrorTriangleDefault(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return 'Error triangle Default'


class ErrorTriangleNotExist(ErrorTriangleDefault):
    def __init__(self, tr: Triangle):
        self.tr = tr

    def __str__(self):
        return f'Треугольник с такими сторонами не существует: {self.tr.__repr__}'


class ErrorTriangleNegativeSide(ErrorTriangleDefault):
    def __init__(self, tr: Triangle):
        self.tr = tr

    def __str__(self):
        res = 'У треугольника отрицательная длина стороны - это недопустимо.\n'
        if self.tr.a < 0:
            res += f'Сторона a={self.tr.a}'
        elif self.tr.b < 0:
            res += f'Сторона b={self.tr.b}'
        elif self.tr.c < 0:
            res += f'Сторона c={self.tr.c}'
        return res

class ErrorTriangleSideNotDefined(ErrorTriangleDefault):
    def __str__(self):
        return f'Сторона треугольника не задана'

while True:
    print('Введите стороны треугольника.')
    try:
        a = int(input('a: '))
    except ValueError as e:
        raise ErrorTriangleSideNotDefined
        break
    try:
        b = int(input('b: '))
    except ValueError as e:
        raise ErrorTriangleSideNotDefined
        break
    try:
        c = int(input('c: '))
    except ValueError as e:
        raise ErrorTriangleSideNotDefined
        break

    tr1 = Triangle(a, b, c)
    print(tr1)
