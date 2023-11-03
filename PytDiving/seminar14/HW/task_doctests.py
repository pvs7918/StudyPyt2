# класс Матрица по 3 теста каждого вида сделать
# асерты, поймать парочку возбуждений


from matrix import Matrix
import doctest


def my_matrix_doctest():
    #тестируем равенство матриц =- дандер метод __eq__
    #тестируем неравенство матриц =- дандер метод __ne__
    """
        >>> Matrix(2, 2, [[1, 2], [3, 4]]) == Matrix(2, 2, [[1, 2], [3, 4]])
        True
        >>> Matrix(2, 2, [[1, 2], [3, 4]]) != Matrix(2, 2, [[1, 2], [3, 5]])
        True
        >>> Matrix(2, 2, [[1, 2], [3, 4]]) + Matrix(2, 2, [[1, 2], [3, 4]]) == Matrix(2, 2, [[2, 4], [6, 8]])
        True
    """
    print("doctest тестирование матриц.")


if __name__ == '__main__':
    doctest.testmod(verbose=True)

