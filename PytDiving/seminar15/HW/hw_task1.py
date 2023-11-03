# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import logging
import sys


class Triangle:
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        # обновляем свойства треугольника
        self._set_properties()

    def _set_properties(self):
        """ делаем проверки допустимости  существования
            и устнавливаем свойства треугольника"""
        if self.a < 0 or \
           self.b < 0 or \
           self.c < 0:
            raise ErrorTriangleNegativeSide(self)

        if (self.a > self.b + self.c) or \
           (self.b > self.a + self.c) or \
           (self.c > self.a + self.b):
            raise ErrorTriangleNotExist(self)
        else:
            # это треугольник. Делаем доп.проверки его сторон
            self.equal_all_sides = False
            self.equal_two_sides = False

            if self.a == self.b and \
               self.b == self.c:
                self.equal_all_sides = True

            elif self.a == self.b or \
                 self.b == self.c or \
                 self.a == self.c:
                self.equal_two_sides = True

    def __str__(self):
        res = f'Треугольник со сторонами: a={self.a}, b={self.b}, c={self.c}, '
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
        # Выводим в лог подробности ошибки
        logging.error(self.__str__())


    def __str__(self):
        return f'Треугольник с такими сторонами не существует: {self.tr.__repr__}'


class ErrorTriangleNegativeSide(ErrorTriangleDefault):
    def __init__(self, tr: Triangle):
        self.tr = tr
        # Выводим в лог подробности ошибки
        logging.error(self.__str__())

    def __str__(self):
        res = 'У треугольника отрицательная длина стороны - это недопустимо. '
        if self.tr.a < 0:
            res += f'Сторона a = {self.tr.a}'
        elif self.tr.b < 0:
            res += f'Сторона b = {self.tr.b}'
        elif self.tr.c < 0:
            res += f'Сторона c = {self.tr.c}'
        return res


class ErrorTriangleSideNotDefined(ErrorTriangleDefault):
    def __init__(self):
        # Выводим в лог подробности ошибки
        logging.error(self.__str__())

    def __str__(self):
        return f'Сторона треугольника не задана'


if __name__ == "__main__":
    # включаем логгирование
    logging.basicConfig(filename='hwtask1.log', filemode='a',
                        encoding='utf-8', level=logging.INFO)

    # если стороны треугольника заданы через командную строку, то они используются,
    # иначе программа работает в интерактивном режиме (запрос сторон треугольника через консоль)

    # Для запуска с параметрами в IDE PyCharm: Run\Run...\Edit Configurations...\Parameters
    # там прописать параметры через пробел, которые помещаются в sys.argv начиная с 1-го элемента
    # Примеры:
    # 5 4 3
    # 2 1 7
    # 7 -1 7

    if len(sys.argv) == 4:
        tr1 = Triangle(sys.argv[1], sys.argv[2], sys.argv[3])
        print(tr1)
        # записываем подробности в лог-файл
        logging.info(tr1)

    else:
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
            # записываем подробности в лог-файл
            logging.info(tr1)
