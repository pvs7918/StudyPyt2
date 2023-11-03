# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

import random


class Matrix:
    """Класс для работы с матрицами и выполнения операций над ними"""

    def __init__(self, a: int, b: int, matrix: list = []):
        self.a = a
        self.b = b
        if self.a < 1 or self.b < 1:
            self.matrix = None
        elif matrix == []:
            self._fill_matrix()  # наполняем матрицу случайными значениями
        else:
            self.matrix = matrix

    def _fill_matrix(self):
        self.matrix = []
        """Наполнение матрицы случайными значениями от 0 до 10 (для примера)"""
        for i in range(self.a):
            cur_row = []
            for j in range(self.b):
                cur_row.append(random.randint(0, 10))
            self.matrix.append(cur_row)

    def sum_all(self):
        """сумма всех элементов матрицы"""
        sum = 0
        for i in range(self.a):
            for j in range(self.b):
                sum += self.matrix[i][j]
        return sum

    def __str__(self):
        """дандер-метод вывода данных объекта для пользователя"""
        res_str = f'Матрица ({self.a}Х{self.b})\n'
        for i in range(self.a):
            res_str += ", ".join(map(str, self.matrix[i])) + '\n'
        res_str += 'сумма элементов = ' + str(self.sum_all()) + '\n'
        return res_str

    def __repr__(self):
        """дандер-метод вывода данных объекта для программиста"""
        res_str = '\n'
        for i in range(self.a):
            res_str += ", ".join(map(str, self.matrix[i])) + '\n'
        res_str += 'сумма элементов = ' + str(self.sum_all()) + '\n'
        return res_str

    def __add__(self, other):
        """метод сложения матриц. сложить можно только матрицы одинаковой размерности"""
        res_matrix = []
        if self.a == other.a and self.b == other.b:
            for i in range(self.a):
                cur_row = []
                for j in range(self.b):
                    cur_row.append(self.matrix[i][j] + other.matrix[i][j])
                res_matrix.append(cur_row)
            return Matrix(self.a, self.b, res_matrix)
        return None

    def __mul__(self, other):
        """метод умножения матриц. self(a,b) X other(a,b). Условие: s.b=o.a"""
        res_matrix = []
        if self.b == other.a:
            for i in range(self.a):
                cur_row = []
                for j in range(other.b):
                    cur_sum = 0
                    for k in range(self.b):
                        cur_sum += self.matrix[i][k] * other.matrix[k][j]
                    cur_row.append(cur_sum)
                res_matrix.append(cur_row)
            return Matrix(self.a, self.b, res_matrix)
        return None

    def __eq__(self, other):
        """дандер-метод сравнения матриц на равенство - каждые элементы сравниваются"""
        if self.a == other.a and self.b == other.b:
            for i in range(self.a):
                for j in range(self.b):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        return False

    def __ne__(self, other):
        """дандер-метод сравнения матриц на неравенство"""
        if self.a == other.a and self.b == other.b:
            for i in range(self.a):
                for j in range(self.b):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return True
            return False
        return True

    def __gt__(self, other):  # больше
        """ дандер-метод сравнения матриц - "больше".
            сравниваются суммы всех элементов матриц"""
        return self.sum_all() > other.sum_all()

    def __ge__(self, other):  # больше или равно
        """ дандер-метод сравнения матриц - "больше или равно".
            сравниваются суммы всех элементов матриц"""
        return self.sum_all() >= other.sum_all()

    def __lt__(self, other):  # меньше
        """ дандер-метод сравнения матриц - "меньше".
            сравниваются суммы всех элементов матриц"""
        return self.sum_all() < other.sum_all()

    def __le__(self, other):  # меньше или равно
        """ дандер-метод сравнения матриц - "меньше или равно".
            сравниваются суммы всех элементов матриц"""
        return self.sum_all() <= other.sum_all()


if __name__ == '__main__':
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    m3 = Matrix(3, 5)
    m4 = Matrix(3, 4)
    m5 = Matrix(3, 4)

    print('Исходные данные:')
    print(f'{m1 = }')  # вывод данных в виде для программиста (метод __repr__())
    print(f'{m2 = }')
    print(f'{m3 = }')
    print(f'{m4 = }')
    print(f'{m5 = }')

    # Сложение
    print('Результаты сложения:')
    print(f'{m1+m2 = }')
    print(f'{m1+m3 = }')

    # Сравнение
    print('\nРезультаты сравнения матриц:')
    print(f'{m1>m2 = }')
    print(f'{m1<m2 = }')
    print(f'{m1==m1 = }')
    print(f'{m1==m2 = }')
    print(f'{m1==m4 = }')
    print(f'{m1!=m1 = }')
    print(f'{m1!=m2 = }')
    print(f'{m1<=m2 = }')
    print(f'{m1>=m2 = }')

    # Умножение
    print('\nРезультаты умножения матриц:')
    print(f'{m1*m2 = }')
    print(f'{m1*m3 = }')
