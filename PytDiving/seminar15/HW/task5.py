# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.
import sys
import logging
from datetime import datetime


def my_parse_date(src_text):
    # функция распознает и возвращает дату из строки текста формата "3-я среда мая" текущего года

    dict_week_day = {'пон': ('Monday', 1), 'вто': ('Tuesday', 2), 'сре': ('Wednesday', 3),
                     'чет': ('Thursday', 4), 'пят': ('Friday', 5), 'суб': ('Saturday', 6),
                     'вос': ('Sunday', 7)}

    dict_for_month = {
        'янв': ('January', 1), 'фев': ('February', 2), 'мар': ('March', 3), 'апр': ('April', 4),
        'мая': ('May', 5), 'июн': ('June', 6), 'июл': ('July', 7), 'авг': ('August', 8),
        'сен': ('September', 9), 'окт': ('October', 10), 'ноя': ('November', 11), 'дек': ('December', 12)
    }

    parse_date = src_text.split()

    if len(parse_date) == 1:
        res_text = f'В дате "{src_text}" всего 1 элемент,а должно быть 2-3: номер недели, день недели  и месяц'
        logging.error(res_text)
        return None, res_text
    if len(parse_date) > 3:
        res_text = f'В дате "{src_text}" больше 3 элементов,а должно быть 2-3: номер недели, день недели и месяц'
        logging.error(res_text)
        return None, res_text

    elif len(parse_date) == 3:  # базовый вариант: заданы все поля - номер недели, день недели, месяц
        # номер недели
        str_week_num = ''
        for ch in parse_date[0]:
            if ch.isdigit():
                str_week_num += ch
        if str_week_num != '':
            parse_week_num = int(str_week_num)
        else:
            res_text = f'В дате "{src_text}" номер недели {parse_date[0]} задан неверно'
            logging.error(res_text)
            return None, res_text

        # день недели
        if parse_date[1][:3] in dict_week_day:
            parse_week_day_name, parse_week_day_num = dict_week_day[parse_date[1][:3]]
        else:
            # проверяем вариант, что день недели задан числом
            if parse_date[1].isdigit():
                parse_week_day_num = int(parse_date[1])
                if not (0 < parse_week_day_num < 8):
                    res_text = f'В дате "{src_text}" день недели {parse_date[1]} задан неверно. Число должно быть' \
                               f' в диапазоне от 1 до 7.'
                    logging.error(res_text)
                    return None, res_text
            else:
                res_text = f'В дате "{src_text}" день недели {parse_date[1]} задан неверно'
                logging.error(res_text)
                return None, res_text

        # месяц
        if parse_date[2][:3] in dict_for_month:
            parse_month, parse_month_num = dict_for_month[parse_date[2][:3]]
        else:
            if parse_date[2].isdigit():
                parse_month_num = int(parse_date[2])
                if not (0 < parse_month_num < 13):
                    res_text = f'В дате "{src_text}" месяц {parse_date[2]} задан неверно. Число должно быть' \
                               f' в диапазоне от 1 до 12.'
                    logging.error(res_text)
                    return None, res_text
            else:
                res_text = f'В дате "{src_text}" месяц {parse_date[2]} задан неверно'
                logging.error(res_text)
                return None, res_text

    # самый сложный вариант. не хватает одного параметра, надо распознать какого
    # и присвоить ему значение по умолчанию
    elif len(parse_date) == 2:
        # номер недели - пытаемся получить число
        str_week_num = ''
        for ch in parse_date[0]:
            if ch.isdigit():
                str_week_num += ch
        if str_week_num != '':
            parse_week_num = int(str_week_num)

            # день недели - задан словом?
            if parse_date[1][:3] in dict_week_day:
                parse_week_day_name, parse_week_day_num = dict_week_day[parse_date[1][:3]]
                parse_month = 1  # присваиваем значение по-умолчанию для месяца
            else:
                # месяц - задан словом?
                if parse_date[1][:3] in dict_for_month:
                    parse_week_day_num = 1
                    parse_month, parse_month_num = dict_for_month[parse_date[1][:3]]
                else:
                    if parse_date[1].isdigit():
                        if 0 < int(parse_date[1]) < 8:
                            parse_week_day_num = int(parse_date[1])
                            parse_month_num = 1
                        elif 7 < int(parse_date[1]) < 13:
                            parse_week_day_num = 1
                            parse_month_num = parse_date[1]
                        else:
                            res_text = f'Дата "{src_text}" не распознается. Недопустимый вариант'
                            logging.error(res_text)
                            return None, res_text
                    else:
                        res_text = f'Дата "{src_text}" не распознается. Недопустимый вариант'
                        logging.error(res_text)
                        return None, res_text

        else:
            # на первой позиции parse_date[0] - не число.
            # Получается это вариант день недели и месяц (словом или числом)
            # номер недели получает значение по-умолчанию = 1
            parse_week_num = 1
            # день недели
            if parse_date[0][:3] in dict_week_day:
                parse_week_day_name, parse_week_day_num = dict_week_day[parse_date[0][:3]]
            else:
                res_text = f'В дате "{src_text}" день недели {parse_date[0]} задан неверно.'
                logging.error(res_text)
                return None, res_text

            # месяц
            if parse_date[1][:3] in dict_for_month:
                parse_month, parse_month_num = dict_for_month[parse_date[1][:3]]
            else:
                if parse_date[1].isdigit():
                    parse_month_num = int(parse_date[1])
                    if not (0 < parse_month_num < 13):
                        res_text = f'В дате "{src_text}" месяц {parse_date[1]} задан неверно. Число должно быть в диапазоне от 1 до 12.'
                        logging.error(res_text)
                        return None, res_text
                else:
                    res_text = f'В дате "{src_text}" месяц {parse_date[1]} задан неверно'
                    logging.error(res_text)
                    return None, res_text

    # год - берем текущий год
    parse_year = datetime.now().year

    # ----вычисляем день месяца
    # день недели первого дня месяца
    cur_text = f'1 {parse_month_num} {parse_year}'
    week_day_for_1day_month = datetime.weekday(datetime.strptime(cur_text, '%d %m %Y')) + 1
    # кортеж d1 содержит номер недели и день недели для 1 числа месяца
    d1 = (1, week_day_for_1day_month)
    # кортеж d2 содержит номер недели и день недели для распознаваемой даты
    d2 = (parse_week_num, parse_week_day_num)

    if d2[1] >= d1[1]:
        parse_day_of_month = (d2[0] - d1[0]) * 7 + (d2[1] - d1[1]) + 1
    else:
        parse_day_of_month = (d2[0] - d1[0] + 1) * 7 + (d2[1] - d1[1]) + 1

    cur_text = f'{parse_day_of_month} {parse_month_num} {parse_year}'
    try:
        cur_date = datetime.strptime(cur_text, '%d %m %Y')
        res_text = f'Исходная дата: {src_text}, результат: {cur_date}, контроли (№ недели, день недели, месяц): ' \
                   f'{parse_week_num}, {parse_week_day_num}, {parse_month_num}'
    except Exception as e:
        logging.error(f'В дате "{src_text}" невозможно распознать дату: {e}. '
                      f' Контроли (№ недели, день недели, месяц): '
                      f'{parse_week_num}, {parse_week_day_num}, {parse_month_num}')
        res_text = f'Исходная дата: {src_text}, результат: None. Смотри лог.'
        cur_date = None

    return cur_date, res_text


if __name__ == "__main__":

    # включаем логгирование
    logging.basicConfig(filename='task5.log', filemode='a',
                        encoding='utf-8', level=logging.INFO)

    # для запуска в командной строке:
    # "3-я пятница июля" "1-й четверг ноября" "3-я среда мая" "5-е воскресенье декабря"
    # "3-я пятница июля" "1-й четверг ноября"
    # нестандартные варианты
    # "3-я 5 июля" "1-й 4 11" "5-е воскресенье 12"
    # неполные варианты
    # "пятница июля" "1-й четверг" "воскресенье 12"

    # если даты заданы через командную строку, то они распознаются, иначе используется список
    if len(sys.argv) > 1:
        date_text_list = sys.argv[1:]
    else:
        date_text_list = ["4-й февраля", "5", "суббота 6", "5-е воскресенье декабря", "5 7 12", "5-е воскресенье 12",
                          "3-я пятница июля", "1-й четверг ноября", "3-я среда мая", "3-я 5 июля", "1-й 4 11"]

    for src_text in date_text_list:
        cur_date, comment = my_parse_date(src_text)
        logging.info(comment)
        print(comment)
