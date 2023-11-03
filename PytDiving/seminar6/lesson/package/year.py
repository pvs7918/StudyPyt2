import sys

def _leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def my_date(date: str):
    day, month, year = list(map(int, date.split('.')))
    if 1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            return _leap_year(year) and day <= 29

def test_dates_argv():
    dates = [i for i in sys.argv][1:]
    if not dates: #  если пустой список
        print('задайте проверяемые даты в при запуске программы в консоле')
    else:
        for date in dates:
            print(date, my_date(date))



if __name__ == '__main__':
    print(my_date('29.02.1984'))

