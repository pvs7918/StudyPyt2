# класс Матрица по 3 теста каждого вида сделать
# асерты, поймать парочку возбуждений

from matrix import Matrix
import unittest


class TestUnitTestMatrix(unittest.TestCase):
    # тестируем класс Matrix

    def setUp(self) -> None:
        "Установка начальных значений матриц"
        self.m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        self.m2 = Matrix(2, 2, [[1, 2], [3, 4]])
        self.m3 = Matrix(2, 2, [[7, 10], [15, 22]])

    def test_equal(self):
        self.assertTrue(self.m1 == self.m2)

    def test_not_equal(self):
        self.assertNotEqual(self.m1, self.m3)

    def test_mult(self):
        self.assertEqual(self.m1 * self.m2, self.m3)


if __name__ == '__main__':
    unittest.main()

    # m1 = Matrix(2, 2, [[1, 2], [3, 4]])
    # m2 = Matrix(2, 2, [[1, 2], [3, 4]])
    # m3 = Matrix(2, 3, [[9, 12, 15], [19, 26, 33]])
    # print(f'{m1*m2 = }')

    # print('Исходные данные:')
    # print(f'{m1 = }')  # вывод данных в виде для программиста (метод __repr__())
    # print(f'{m2 = }')
    # print(f'{m3 = }')
    # print(f'{m4 = }')
    # print(f'{m5 = }')
    #
    # # Сложение
    # print('Результаты сложения:')
    # print(f'{m1+m2 = }')
    # print(f'{m1+m3 = }')
    #
    # # Сравнение
    # print('\nРезультаты сравнения матриц:')
    # print(f'{m1>m2 = }')
    # print(f'{m1<m2 = }')
    # print(f'{m1==m1 = }')
    # print(f'{m1==m2 = }')
    # print(f'{m1==m4 = }')
    # print(f'{m1!=m1 = }')
    # print(f'{m1!=m2 = }')
    # print(f'{m1<=m2 = }')
    # print(f'{m1>=m2 = }')
    #
    # # Умножение
    # print('\nРезультаты умножения матриц:')
    # print(f'{m1*m2 = }')
    # print(f'{m1*m3 = }')
