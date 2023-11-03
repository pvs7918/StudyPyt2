# 3. В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания и
# регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

text = """Белый праздник — рождается предвечное Слово,
белый праздник идет, и снова —
вместо елочной, восковой свечи,
бродят белых прожекторов лучи,
мерцают сизые стальные мечи
вместо елочной, восковой свечи.

Белый, белый, белый снег!
свечи, мечи, сизые,           сизые!!! сизые сизые сизые сизые сизые"""

bad_symbols = ",.!?-—\n"

nice_text = text.lower()  # приводим к нижнему регистру

# заменяем ненужные знаки препинания на пробелы
for ch in bad_symbols:
    nice_text = nice_text.replace(ch, ' ')

# убираем множественные пробелы, заменяем их на простые пробелы

space_cnts = set()  # наличие какого количества пробелов в файле
prev_symb = ''
cur_space_count = 0
for ch in nice_text:
    if ch == ' ':
        cur_space_count += 1
    else:
        if prev_symb == ' ':
            if cur_space_count > 1:
                space_cnts.add(cur_space_count)
            cur_space_count = 0
    prev_symb = ch

# в первую очередь убираем самые длиные последовательности пробелов
space_cnts = sorted(space_cnts, reverse=True)

# заменяем последовательности пробелов на простые пробелы
for i in space_cnts:
    nice_text = nice_text.replace(' ' * i, ' ')

#разбивка на слова
all_words = nice_text.split()
#набор слов
words_set = set(all_words)

# в словарь помещаем количество повторов каждого слова
words_count = {}
# находим количество вхождений слов в тексте
for cur_word in words_set:
    words_count[cur_word] = all_words.count(cur_word)

# получаем список самых часто упоминаемых слов
most_popular_words_list = sorted(words_count, key=words_count.get,
                                 reverse=True)

print(f'Самые частые 10 слов в тексте:')
for cur_word in most_popular_words_list[:10]:
    print(f'Слово:{cur_word} - повторов:{words_count[cur_word]}')
