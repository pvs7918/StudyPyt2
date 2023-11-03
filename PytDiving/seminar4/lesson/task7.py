# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def my_sum(lst):
    summ = 0
    for val in lst:
        summ += val
    return summ


print('Промежуточные итоги (для проверки программы):')


def get_summs(dict_companies) -> list:
    res_list = []
    for k, value in dict_companies.items():
        cur_summ = sum(value)
        res_list.append(cur_summ > 0)
        print(f'Компания {k}=, сумма расходов={cur_summ}, Расходы>0? = {cur_summ > 0}')
    return res_list


dict_companies = {'РосПромФлот': (10000, 20000, 15000),
                  'ДальСнабРесурс': (-100000, -20000, 30000, 200000),
                  'СеверГазТранс': (-200000, 300250, 10000)}

# формируем список в котором булеове значение - сумма затрат комании больше или меньше 0.
list_CompaniesSummMoreZero = get_summs(dict_companies)

print('Итог:')

if all(list_CompaniesSummMoreZero):
    print('Все компании прибыльные!')
else:
    print('Одна или несколько из компаний убыточные!')
