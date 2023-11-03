# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def calc_summ(names: list[str], stavki: list[int], percents: list[str]):
    res_dict = {}
    for cur_name, cur_stavka, cur_percent in zip(names, stavki, percents):
        res_dict[cur_name] = cur_stavka * float(cur_percent[:-1]) / 100
    return res_dict


names = ['Ivan', 'Stepan', 'Fedor']
stavki = [10000, 25000, 8000]
percents = ['5.5%', '10.4%', '7.9%']

print(calc_summ(names, stavki, percents))
