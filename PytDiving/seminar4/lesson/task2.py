# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

txt = "Исходная строка текста"

def sorted_unicode_symblos(text):
    my_list = []
    for i in text:
        if ord(i) not in my_list:
            my_list.append(ord(i))
    my_list.sort()
    return my_list

print(sorted_unicode_symblos(txt))