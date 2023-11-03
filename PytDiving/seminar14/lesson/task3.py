# 📌Напишите для задачи 1 тесты unittest.
# Проверьте следующие варианты:
# 📌возврат строки без изменений
# 📌возврат строки с преобразованием регистра без потери символов
# 📌возврат строки с удалением знаков пунктуации
# 📌возврат строки с удалением букв других алфавитов
# 📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_lowercase
import unittest


def removal_chars(text: str) -> str:
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + ' ':
            result += ch

    return result


class TestFunc(unittest.TestCase):
    def test_1(self):
        self.assertTrue(removal_chars("wefg") == "wefg")

    def test_2(self):
        self.assertEqual(removal_chars("we,,!f.g") , "wefg")

    def test_3(self):
        self.assertFalse(removal_chars("WERtЕР") == "WERtер")

    def test_4(self):
        self.assertEqual(removal_chars("we,, !f.gЕРJ"), "we fgj")


if __name__ == '__main__':
    unittest.main()
