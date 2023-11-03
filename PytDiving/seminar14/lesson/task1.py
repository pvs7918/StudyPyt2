# 📌 Создайте функцию, которая удаляет из текста все символы кроме
#  букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

from string import ascii_lowercase


def removal_chars(text: str) -> str:
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + ' ':
            result += ch

    return result