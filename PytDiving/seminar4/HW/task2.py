# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def get_key_params(**kwargs):
    res_dict = {}

    for k, val in kwargs.items():
        try:
            if hash(val):   # если значение имеет хэш
                res_dict[val]=k
        except Exception as ex:
            res_dict[str(val)]=k

    return res_dict



print('Результат')
print(get_key_params(name1=2, param2="тест", param3="digest"))
