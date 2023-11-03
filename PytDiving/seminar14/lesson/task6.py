# 📌На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# 📌Напишите 3-7 тестов pytest для данного проекта.
# 📌Используйте фикстуры.

import pytest
from square import Square



@pytest.fixture
def fix():
    sq = Square(18, 7)
    return sq

def test_1(fix):
    assert fix.perimeter() == 50

def test_2(fix):
    with pytest.raises(ValueError):
        fix.length = -10

if __name__ == "main":
    pytest.main(["-v"])