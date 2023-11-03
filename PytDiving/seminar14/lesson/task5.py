# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

from square import Square
import unittest


class TestSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.test_sq = Square(10, 5)
        self.test_kvad = Square(10)

    def test_1(self):
        self.assertEqual(self.test_kvad.b, 10)

    def test_2(self):
        self.assertFalse(self.test_kvad.b is None)

    def test_area(self):
        self.assertEqual(self.test_sq.square(), 50)

    def test_perimeter(self):
        self.assertEqual(self.test_sq.perimeter(), 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
