# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.
import logging
from datetime import datetime


def my_parse_date(src_text):
    # функция распознает и возвращает дату из строки текста формата "3-я среда мая" текущего года

    dict_week_day = {'пон': ('Monday', 1), 'вто': ('Tuesday', 2), 'сре': ('Wednesday', 3),
                     'чет': ('Thursday', 4), 'пят': ('Friday', 5), 'суб': ('Saturday', 6),
                     'вос': ('Sunday', 7)}

    dict_for_month = {
        'янв': 'January', 'фев': 'February', 'мар': 'March', 'апр': 'April',
        'мая': 'May', 'июн': 'June', 'июл': 'July', 'авг': 'August',
        'сен': 'September', 'окт': 'October', 'ноя': 'November', 'дек': 'December'
    }

    parse_date = src_text.split()
    # номер недели
    str_week_num = ''
    for ch in parse_date[0]:
        if ch.isdigit():
            str_week_num += ch
    if str_week_num != '':
        parse_week_num = int(str_week_num)
    else:
        logging.error(f'В дате "{src_text}" номер недели {parse_date[0]} задан неверно')
        return None
    # день недели
    if parse_date[1][:3] in dict_week_day:
        parse_week_day_name, parse_week_day_num = dict_week_day[parse_date[1][:3]]
    else:
        logging.error(f'В дате "{src_text}" день недели {parse_date[1]} задан неверно')
        return None
    # месяц
    if parse_date[2][:3] in dict_for_month:
        parse_month = dict_for_month[parse_date[2][:3]]
    else:
        logging.error(f'В дате "{src_text}" месяц {parse_date[2]} задан неверно')
        return None
    # год
    parse_year = datetime.now().year

    # ----вычисляем день месяца
    # день недели первого дня месяца
    cur_text = f'1 {parse_month} {parse_year}'
    week_day_for_1day_month = datetime.weekday(datetime.strptime(cur_text, '%d %B %Y')) + 1
    # кортеж d1 содержит номер недели и день недели для 1 числа месяца
    d1 = (1, week_day_for_1day_month)
    # кортеж d2 содержит номер недели и день недели для распознаваемой даты
    d2 = (parse_week_num, parse_week_day_num)

    if d2[1] >= d1[1]:
        parse_day_of_month = (d2[0] - d1[0]) * 7 + (d2[1] - d1[1]) + 1
    else:
        parse_day_of_month = (d2[0] - d1[0] + 1) * 7 + (d2[1] - d1[1]) + 1

    cur_text = f'{parse_day_of_month} {parse_month} {parse_year}'
    try:
        cur_date = datetime.strptime(cur_text, '%d %B %Y')
    except Exception as e:
        logging.error(f'В дате "{src_text}" невозможно распознать дату: {e}')
        return None

    return cur_date


if __name__ == "__main__":

    # включаем логгирование
    logging.basicConfig(filename='task4.log', filemode='a',
                        encoding='utf-8', level=logging.INFO)

    date_text_list = ["3-я пятница июля", "1-й четверг ноября", "3-я среда мая", "6-е воскресенье декабря"]
    for src_text in date_text_list:
        cur_date = my_parse_date(src_text)
        if cur_date == None:
            print(f'Исходный текст даты:{src_text}, вычисленная дата: {cur_date}.')
        else:
            print(f'Исходный текст даты:{src_text}, вычисленная дата: {cur_date}, контроль(день недели):'
              f'{datetime.weekday(cur_date) + 1}')
