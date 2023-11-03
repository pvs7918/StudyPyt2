# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate,
# list comprehension
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
#
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
#
# out
# The data is incorrect

from random import sample


def Create_SampleText(count: int, elem_len: int, letters: str):
    res_list = []

    if count < 1:
        return []
    for i in range(count):
        # случайным образом выбираем elemLen букв из словаря Letters
        #объединяем буквы в строку и помещаем в список
        res_list.append("".join(sample(letters, elem_len)))
    return " ".join(res_list)

def DelElemFromListByExamle(txt:str, delExample:str):
    #переформируем список с помощью list comprehention с условием
    #по условию задачи исходные данные в виде текста и результат тоже текстовая строка
    ls = txt.split(' ')
    ls = [i for i in ls if i != delExample]
    return " ".join(ls)

N = int(input('Введите количество слов: '))
srcStr = "абв"
ls = Create_SampleText(N, 3, srcStr)
print(ls)
ls2 = DelElemFromListByExamle(ls, srcStr)
print(f'После удаления "{srcStr}":')
print(ls2)


