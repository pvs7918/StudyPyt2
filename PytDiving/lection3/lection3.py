# # Списки
# # Способы объявления списков
# list_1 = list()
# list_2 = list((3.14, True, "Hello world!"))
# list_3 = []
# list_4 = [3.14, True, "Hello world!"]


# Метод append
# Для добавления нового элемента в конец списка используется метод append
# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a)
# print(my_list)
# my_list.append(b)
# 8
# print(my_list)
# my_list.append(c)
# print(my_list)


# Метод extend
# Метод extend ведёт себя аналогично append, то есть добавляет элементы в конец
# списка. В качестве аргумента extend принимает последовательность, итерируется
# по ней слева направо и каждый элемент добавляет в новую ячейку списка.
# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.extend(a) # TypeError: 'int' object is not iterable
# print(my_list)
# my_list.extend(b)
# print(my_list)
# my_list.extend(c)
# print(my_list)
# my_list.extend(my_list)
# print(my_list)

# ● extend(a) — если в метод передать не коллекцию, получим ошибку TypeError.
# ● extend(b) — строка воспринимается как коллекция, в результате каждый
# символ строки помещается в новую ячейку списка.
# ● extend(c) — итерируемся по списку, c последовательно добавляя его
# элементы в список my_list
# ● extend(my_list) — удваиваем список, добавляя копию всех его элементов.


# Метод pop
# Метод pop позволяет удалить элемент списка. Удаляемый элемент возвращается
# как результат работы метода.
# pop() - удалит последний элемент

# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list)
# eggs = my_list.pop(1)
# print(eggs, my_list)
# err = my_list.pop(10) # IndexError: pop index out of range


# Метод count
# Метод count подсчитывает вхождение элемента в список.
# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.count(2)
# print(spam)
# eggs = my_list.count(3)
# print(eggs)
# Метод принимает именно объект, а не индекс. Если объект отсутствует в списке,
# count возвращает ноль — элемент был встречен в списке ноль раз.
# Count имеет линейную асимптотику O(n), т.к. для подсчёта метод перебирает все
# элемента списка и сравнивает их с переданным объектом.


# Метод insert
# Метод insert принимает на вход два аргумента — индекс для вставки и объект
# вставки. Метод добавляет элемент после индекса.
# my_list = [2, 4, 6, 8, 10, 12]
# my_list.insert(2, 555)
# print(my_list)
# my_list.insert(-2, 13)
# print(my_list)
# my_list.insert(42, 73) # my_list.append(73)
# print(my_list)
# Если индекс положительный, элемент добавляется в указанную ячейку, а все
# последующие элементы списка сдвигаются на ячейку правее.
# Если индекс отрицательный, отсчитывается необходимое количество элементов
# справа для вставки. Например -2 означает, что после вставки справа от
# добавленного элемента будет находится ещё два.
# В том случае, когда индекс оказывается больше, чем количество элементов списка,
# объект добавляется в конец. В таком случае логичнее использовать метод append,
# выполняющий добавление элемента в конец списка.

# Метод remove
# Метод remove принимает на вход объект, производит его поиск в списке и удаляет в
# случае нахождения.
# my_list = [2, 4, 6, 8, 10, 12, 6]
# my_list.remove(6)
# print(my_list)
# my_list.remove(3) # ValueError: list.remove(x): x not in list
# print(my_list)
# Если удаляемый элемент встречается в списке несколько раз, удаляется только
# один элемент — самый левый.
# А если удаляемый элемент отсутствует в списке, будет вызвана ошибка ValueError.

# Функция sorted()
# Функция sorted принимает на вход любую коллекцию по которой можно
# итерироваться и возвращает отсортированный список.
# 🔥 Важно! Функция sorted может принимать не только списки, но и другие
# последовательности: строки, множества, кортежи, словари и т.п.. При этом
# функция всегда возвращает список.
# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list)
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True)
# print(my_list, rev_list, sep='\n')
# Переданная в функцию коллекция остаётся неизменной после результата работы
# функции. Если в функцию передать дополнительный аргумент reverse=True,
# сортировка происходит по убыванию.
# Внутри функции используется алгоритм сортировки Timsort — гибридная
# устойчивая сортировка с временной асимптотикой O(n log n). Дополнительно
# тратится O(n) памяти на создание нового отсортированного списка.

# Метод sort()
# Метод sort осуществляет сортировку элементов списка без создания копии, inplace.
# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)
# Как и функция sorted метод sort упорядочивает элементы по возрастанию. Если
# передать дополнительный параметр reverse=True, будет произведена сортировка по
# убыванию. Внутри метода работает тот же самый алгоритм сортировки Timsort. Но
# память на создание копии списка мы не тратим.




# Метод reverse() и синтаксический сахар [::-1]
# Если нам нужно развёрнутая версия списка логичные и удобнее использовать
# встроенный метод reverse.
# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.reverse()
# print(my_list)
# Метод разворачивает список на месте не создавая копии.
# Кроме этого в Python есть возможность получить развернутую копию через особую
# запись в квадратных скобках, синтаксический сахар. После имени списка в
# квадратных скобках слитно записываем два двоеточия и минус один.
# my_list = [4, 8, 2, 9, 1, 7, 2]
# new_list = my_list[::-1]
# print(my_list, new_list, sep='\n')
#
#
# Срезы
# Используя квадратные скобки можно делать частичные копии списка - срезы.
# Базовый синтаксис следующий.
# list[start:stop:step]
# start указывает на первый индекс, который включается в срез. При отсутствии
# значения start равен нулю, началу списка.
# stop указывает на последний индекс, который не включается в срез. При отсутствии
# значения stop равен последнему элементу списка и включает его в срез.
# step — шаг движения от star до stop. По умолчанию step равен единице, все
# элементы по порядку.
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:7:2])
# print(my_list[:7:2])
# print(my_list[2::2])
# print(my_list[2:7:])
# print(my_list[8:3:-1])
# print(my_list[3::])
# print(my_list[:7:])

# Зачем нужна функция copy.deepcopy()
# Иногда программисту приходится работать с вложенными друг в друга
# коллекциями. Например матрица или список списков.
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')
# Метод copy создал поверхностную копию, копию верхнего уровня. Изменения же
# вложенных объектов отразится и на оригинале. В таком случае для создания
# полной копии любой глубины вложенности используют функцию deepcopy из
# модуля copy.
# import copy
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = copy.deepcopy(matrix)
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')
# Функция рекурсивно обходит все вложенные объекты создавая их копии.
# Изменения одной коллекции теперь не затрагивают её копию.


# Функция len
# В финале списков рассмотрим функцию len. На вход она принимает любую
# коллекцию, в которой можно посчитать количество элементов.
# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(len(my_list))
# print(len(matrix))
# print(len(matrix[1]))



# Работа со строками как с массивами
# text = 'Hello world!'
# print(text[6])
# print(text[3:7])
# Индексы и срезы работают аналогично спискам.
# Если необходимо заменить элемент новым, индексы не подойдут. Для этих целей
# нужен метод replace
# 19
# new_txt = text.replace('l', 'L', 2)
# print(text, new_txt, sep='\n')

# Методы count, index, find
# Как и у списка, строка поддерживает методы count для подсчёта вхождения и index
# для поиска элемента. Но у строки появился и новый метод find. Он работает
# аналогично index. Но если искомая подстрока отсутствует, вместо ошибки
# возвращает -1.
# text = 'Hello world!'
# print(text.count('l'))
# print(text.index('l'))
# print(text.find('l'))
# print(text.find('z'))

# Реверс строк
# Для разворота строки используется обратный срез, как и в случае со списком.
# text = 'Hello world!'
# print(text[::-1])


# Уточнение формата
# Существую различные способы уточнения способа вывода значения переменной.
# pi = 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}')
# data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
# for item in data:
# print(f'{item:>10}')
# 22
# num = 2 * pi * data[1]
# print(f'{num = :_}')
# После указания имени переменной в фигурных скобках ставится двоеточие —
# указатель на символы задания формата далее.
# ● :.2f — число пи выводим с точность два знака после запятой
# ● :>10 — элементы списка выводятся с выравниванием по правому краю и
# общей шириной вывода в 10 символов
# ● = — выводим имя переменной, знак равенства с пробелами до и после него и
# только потом значение.
# ● :_ — число разделяется символом подчёркивания для деления на блоки по 3
# цифры.


# метод split
#
# link = 'https://habr.com/ru/users/dzhoker1/posts/'
# urls = link.split('/')
# print(urls)
# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)
#
# a, b, c, *_ = input('Введите не менее трёх чисел через пробел:
# ').split()



# Метод join
# Метод join принимает на вход итерируемую последовательность и соединяет все её
# элементы в строку, разделяя каждый текстом, к которому применён метод. В
# некоторой степени join противоположен split.
# data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1',
# 'posts']
# url = '/'.join(data)
# print(url)
# К строке “/” применили метод, т.е. каждый элемент списка будет разделён слешем.
# При этом в начале и в конце получившейся строки слеша не будет.


# Методы upper, lower, title, capitalize
# При работе с текстом можно быстро менять строчные буквы на прописные и
# наоборот.
# 24
# text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# ● upper — все символы приводятся к верхнему регистру
# ● lower — все символы приводятся к нижнему регистру
# ● title — первый символ каждого слова (разделитель слов - пробел) приводится
# к верхнему регистру, остальные символы к нижнему
# ● capitalize — первый символ строки в верхнем регистре, остальные в нижнем

# Методы startswith и endswith
# Метод startswith проверяет начинается ли строка с заданной подстроки. Метод
# возвращает истину или ложь. Метод endswith проверяет окончание строки
# переданной в качестве аргумента подстрокой.
# text = 'Однажды в студёную зимнюю пору'
# print(text.startswith('Однажды'))
# print(text.endswith('зимнюю', 0, -5))
# Оба метода помимо подстроки могут принимать параметры start и stop. В этом
# случае проверка начала либо конца будет проводиться в указанном диапазоне.


# text = 'Привет, мир!'
# print(text.find(' '))
# print(text.title())
# print(text.split())
# print(f'{text = :>25}')
#
#
#
# Кортеж, tuple
# Кортежи — это неизменяемые последовательности, обычно используемые для
# хранения коллекций разнородных данных. Также используются в случаях, когда
# требуется неизменяемая последовательность однородных данных. Как и строку
# кортеж нельзя изменить после создания. При этом кортеж как и список является
# массивом указателей на объекты любого типа.
# Способы создания кортежа
# Создать кортеж можно четырьмя способами.
# a = ()
# b1 = 1,
# b2 = (1,)
# c1 = 1, 2, 3,
# c2 = (1, 2, 3)
# d = tuple(range(3))
# print(a, b1, b2, c1, c2, d, sep='\n')
# 1. Пара круглых скобок создаёт пустой кортеж
# 2. Один элемент с замыкающей запятой в скобках или без них создаёт кортеж с
# элементом
# 3. Несколько элементов разделенных запятыми с замыкающей запятой или в
# круглых скобках
# 4. Функция tuple(), которой передаётся любой итерируемый объект
# 🔥 Важно! Обратите внимание, что на самом деле кортеж образует запятая,
# а не круглые скобки. Круглые скобки необязательны, за исключением случая
# пустого кортежа или когда они необходимы, чтобы избежать синтаксической
# неоднозначности. Например, f(a, b, c) — это вызов функции с тремя
# аргументами. f((a, b, c)) — вызов функции с кортежем в качестве
# единственного аргумента.

# Кортежи реализуют все общие операции
# последовательностей
# ● Обращение к элементу по индексу
# ● Срезы
# ● Методы, которые работают с последовательностью, но не меняют её: count,
# index, а также функция len()


# 4. Словарь, dict
# В Python есть изменяемый тип данных словарь. В других языках аналогичная
# структура данных может называться отображение, mapping, именованный массив,
# ассоциативный массив, сопоставление и т.п. Словарь представляет набор пар
# ключ-значение. Ключ — любой неизменяемый тип данных. Значение - любой тип
# данных. Обращаясь к ключу словаря получают доступ к значению.
# 🔥 Важно! Ключ выступает источником для вычисления хеша. Полученный
# хеш играет роль числового индекса и указывает на ячейку со значением. В
# Python вычисление хеша возможно лишь у неизменяемых типов данных.
# Следовательно, ключ словаря обязан быть неизменяемым объектом. Обычно
# это строка, целое число (вещественные лучше не использовать, вы же помните
# о точности округления), либо кортеж или неизменяемое множество.
#
# Способы создания словаря
# Для создания словаря есть несколько способов. Например:
# ● передать набор пар ключ-значение в фигурных скобках,
# ● использовать знак равенства между ключом и значением,
# ● передать любую последовательность, каждый элемент который пара ключ и
# значение
# a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
# b = dict(one=42, two=3.14, ten='Hello world!')
# c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
# print(a == b == c)
# Все три способа создают одинаковые словари.
# 🔥 Важно! Вариант b не допускает использования зарезервированных слов.
# При этом ключи указываются без кавычек, но в словаре становятся ключами
# типа str.

# Добавление нового ключа
# Для добавления в существующий словарь новой пары ключ-значение можно
# использовать обычную операцию присваивания.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# my_dict['ten'] = 10
# print(my_dict)
# Доступ к значению словаря
# Доступ через квадратные скобки []
# Для получения доступа к значению необходимо указать ключ в квадратных скобках
# после или переменной.
# 28
# TEN = 'ten'
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict['two'])
# print(my_dict[TEN])
# print(my_dict[1]) # KeyError: 1
# Ключ может быть указан явно или передам как содержимое переменной,
# константы. При попытке обратиться к несуществующему ключу получаем ошибку:
# KeyError.
# Доступ к ключу позволяет изменять значения. Для этого используем операцию
# присваивания как и в случае с добавлением новой пары ключ-значение.

# Доступ через метод get
# Если ли мы хотим гарантировать отсутствие ошибки KeyError при обращении к
# элементу словаря, можно обратиться к значению через метод get, а не квадратные
# скобки.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.get('two'))
# print(my_dict.get('five'))
# print(my_dict.get('five', 5))
# print(my_dict.get('ten', 5))
# При обращении к существующему ключу метод get работает аналогично доступу к
# через квадратные скобки. Если обратиться к несуществующему ключу, get
# возвращает None. Метод get принимает второй аргумент, значение по умолчанию.
# Если ключ отсутствует в словаре, вместо None будет возвращено указанное
# значение.

# Метод setdefault
# Метод setdefault похож не get, но отсутствующий ключ добавляется в словарь.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.setdefault('five')
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.setdefault('six', 6)
# print(f'{eggs = }\t{my_dict=}')
# new_spam = my_dict.setdefault('two')
# print(f'{new_spam=}\t{my_dict=}')
# new_eggs = my_dict.setdefault('one', 1_000)
# print(f'{new_eggs=}\t{my_dict=}')
# При вызове метода с одним аргументом отсутствующий ключ добавляется в
# словарь. В качестве значения передаётся None. Если указать два аргумента и ключ
# отсутствует, второй аргумент становится значением ключа и также добавляется в
# словарь. При обращении к существующему ключу, словарь не изменяется
# независимо от того указанные один или два аргумента.

# Метод keys
# Метод keys возвращает объект-итератор dict_keys.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.keys())
# for key in my_dict.keys():
# print(key)
# Обычно объект не используют напрямую. Метод keys применяется в связке с
# циклом for для перебора ключей словаря.

# Метод values
# Метод values похож на keys, но возвращает значения в виде объекта итератора
# dict_values, а не ключи.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.values())
# for value in my_dict.values():
# print(value)


# Метод items
# Если в цикле необходимо работать одновременно с ключами и значениями, как с
# парами, используют метод items.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.items())
# for tuple_data in my_dict.items():
# print(tuple_data)
# for key, value in my_dict.items():
# print(f'{key = } value before 100 - {100 - value}')
# Метод возвращает объект итератор dict_items. Если создать цикл for с одной
# переменной между for и in, получим кортеж из пар элементов — ключа и значения.
# Обычной используют две переменные в цикле: первая принимает ключ, а вторая
# значение. Такой подход облегчает чтение кода и позволяют использовать ключ и
# значение по-отдельности.

#
# Метод popitem
# Для удаления пары ключ значение из словаря используют метод popitem.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.popitem()
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.popitem()
# print(f'{eggs = }\t{my_dict=}')
# Так как словари сохраняют порядок добавления ключей, удаление происходит
# справа налево, по методу LIFO. Элементы удаляются в обратном добавлению
# порядке.
# 🔥 Важно! Если измените значение у существующего ключа, положение
# ключа в очереди не меняется, он не считается последним добавленным.

# Метод pop
# Метод pop удаляет пару ключ-значение по переданному ключу.
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.pop('two')
# print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six') # KeyError: 'six'
# err = my_dict.pop() # TypeError: pop expected at least 1
# argument, got 0
# Если указать несуществующий ключ, получим ошибку KeyError. В отличии от метода
# pop у списков list, dict.pop вызовет ошибку TypeError. Для удаление последнего
# элемента нужен метод popitem.


# 5. Множества set и frozenset
# Ещё одна коллекция из коробки — множества. Множество — набор уникальных
# неиндексированных элементов. В Python есть два вида множеств: set —
# изменяемое множество, frozenset — неизменяемое множество. Неизменяемое
# множество позволяет вычислять хеш и может использоваться там, где разрешён
# 33
# лишь хешированный тип данных, например в качестве ключа словаря.
# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set)
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'
# Обратите внимание, что двойка передавалась в множества дважды, но хранится в
# единственном экземпляре, как один из уникальных элементов
# 🔥 Важно! Элементом множества могут быть только неизменяемые типы
# данных.

# Методы множеств
# Рассмотрим некоторые методы множеств на примере изменяемого множества set.
# Все методы, которые не изменяют оригинал, работают аналогично и для множества
# frozenset.
# Метод add
# Метод add работает аналогично методу списка append, т.е. добавляет один элемент
# в коллекцию.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.add(9)
# print(my_set)
# my_set.add(7)
# print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one
# argument (2 given)
# my_set.add((9, 10))
# print(my_set)

# Метод remove
# Для удаления элемента множества используют метод remove.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.remove(5)
# print(my_set)
# my_set.remove(10) # KeyError: 10
# При передаче несуществующего объекта получим ошибку KeyError.
# Метод discard
# Метод discard работает аналогично remove — удаляет один элемент множества.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.discard(5)
# print(my_set)
# my_set.discard(10)
# В отличии от remove при попытке удалить несуществующий элемент discard не
# вызывает ошибку. При этом множество не изменяется.

# Метод intersection
# Для получения пересечения множеств, т.е. множества с элементами, которые есть и
# в левом и в правам множестве используют метод intersection
# 35
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.intersection(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# Новая версия Python позволяет получить пересечение множеств в следующей
# записи c использованием символа &
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set & other_set
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

# Внимание! Исходные множества при пересечении не изменяются.

# Метод union
# Для объединения множеств используется метод union.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set | other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
# На выходе получаем множество уникальных элементов из левого и правого
# множеств. Более короткая запись объединения возможна при помощи
# вертикальной черты.

# Метод difference
# Метод difference удаляет из левого множества элементы правого.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.difference(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set - other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
# На выходе получаем множество элементов встречающихся только в левом
# множестве. Более короткая запись возможно при помощи знака минус. Вычитаем
# из левого элементы правого.

# Проверка на вхождение, in
# Для проверки входит ли элемент в множество используют зарезервированное
# слово in.
# my_set = {3, 4, 2, 5, 6, 1, 7}
# print(42 in my_set)
# 🔥 Внимание! Слово in позволяет сделать проверку на вхождение и в других
# коллекциях. Входит ли объект в list, tuple, является ли подстрока частью строки
# str, встречается ли ключ в словаре. Для list, tuple, str проверка на вхождение
# работает за линейное время O(n). Для dict, set, frozenset проверка работает за
# константное время O(1).