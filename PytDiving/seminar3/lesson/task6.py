# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text = "У нас все хорошо".lower().split()
text.sort()
maxlength = len(max(text, key=len))
# print(maxlength)

for i, elem in enumerate(text, 1):
    print(f'{i} {elem :>{maxlength}}')  # :> выравнивание элемента по правому краю, < по левому