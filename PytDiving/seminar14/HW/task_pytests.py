# класс Матрица по 3 теста каждого вида сделать
# асерты, поймать парочку возбуждений

from matrix import Matrix
import pytest

@pytest.fixture
def matr():
    #словарь матриц возвращаем
    m = {1: Matrix(2, 2, [[1, 2], [3, 4]]),
         2: Matrix(2, 2, [[1, 2], [3, 4]]),
         3: Matrix(2, 2, [[2, 4], [6, 8]])}
    return m

def test_my_1(matr):
    # через фикстуру matr инициализируем словарь матриц, к которым обращаемся по ключу
    assert matr[1] == matr[2]

def test_my_2(matr):
    assert not matr[1] == Matrix(2, 2, [[1, 2], [3, 5]])

def test_my_3(matr):
    assert matr[1] + matr[2] == matr[3]

if __name__ == '__main__':
    pytest.main(['-v'])