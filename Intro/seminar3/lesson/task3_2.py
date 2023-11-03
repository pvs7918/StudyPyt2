# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import choices


def list_rand_words(count: int, alp: str = 'xyz'):
    words_list = []
    for i in range(count):
        letters = choices(alp, k=3)
        words_list.append("".join(letters))
    return words_list


def find_sec(word: str, list_words: list):
    if list_words.count(word) > 1:
        index_w = list_words.index(word)
        print(list_words.index(word, index_w + 1))
    else:
        print(-1)


all_list = list_rand_words(int(input("Number of words: ")))
print(all_list)
find_sec(input("Enter the word: "), all_list)
