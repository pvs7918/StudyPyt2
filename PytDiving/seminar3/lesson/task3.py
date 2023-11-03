# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = {3, 4.5, True, "Hello", 5, False}
my_dict = {}

for i in my_tuple:
    if type(i) not in my_dict:
        my_dict[type(i)] = [i]
    else:
        my_dict[type(i)].append(i)
print(my_dict)
