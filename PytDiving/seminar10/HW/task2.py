# Возьмите задачу о банкомате из семинара. Решить её с помощью объектов.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Задача №3 из ДЗ Семинара 4 переписанная в стиле ООП.

from datetime import datetime


class Client:
    id: str
    fullname: str = None
    account_size: int = 0

    def __init__(self, id: str, fullname: str = None, account_size: int = 0):
        self.id = id
        self.fullname = fullname
        self.account_size = account_size

    def info(self):
        # информация о клиенте для вывода на экран
        return f'id: {self.id}, ' \
               f'ФИО: {self.fullname}, ' \
               f'на счету: {self.account_size}'


class Atm:
    id: str = None
    adress: str = None
    cash_size: int = 0
    oper_count: int = 0

    def __init__(self, id: str = None, adress: str = None,
                 cash_size: int = 0, oper_count: int = 0):
        self.id = id
        self.adress = adress
        self.cash_size = cash_size
        self.oper_count = oper_count

    def info(self):
        # информация о банкомате для вывода на экран
        return f'id: {self.id}, ' \
               f'Адрес: {self.adress},\n' + \
               f'на счету: {self.cash_size}, ' \
               f'количество операций: {self.oper_count}.'


class Operation:
    id: str  # идентификатор операции
    name: str  # название операции: 'внесение', 'снятие'
    src_cash_size: float = 0  # исходная сумма операции
    atm: Atm = None  # банкомат на котором проводится комиссия
    client: Client = None  # клиент, который выполняет комиссию

    # при успешном выполнении операции детали операции помещаем в description,
    # потому что состояние счетов банкомата и клиента меняются
    description: str = 'Не проведена'

    commision: float = 1.5  # размер комиссии
    commision_cash_size: float = 0
    commision_10_percent_size: float = 0  # размер налога на богатство по данной операции (если сумма операции > 5млн.у.е)
    remain_cash_size: float = 0

    def __init__(self, id: str, name: str, src_cash_size: float, atm, client):
        self.id = id
        self.name = name.lower()
        self.src_cash_size = src_cash_size
        self.atm = atms[atm]
        self.client = clients[client]

    def info(self):
        return f'Операция: id: {self.id}, ' \
               f'тип операции: {self.name}, ' + \
               f'сумма операции: {self.src_cash_size}.\n' \
               f'Детали операции:\n{self.description}\n'

    def execute(self):
        if self.name == "внесение":
            self.__put_cash_to_account()
        if self.name == "снятие":
            self.__dispense_cash_to_client()

        print(self.description)

    def __put_cash_to_account(self):
        # внесение наличных на банкомат atm клиентом client.
        # при этом с клиента списывается комиссия в размере commision %

        # размер комиссии по умолчанию
        self.commision = 1.5

        # Печатаем предварительную информацию, перед выполнением операции
        txt_ = 'Операция - Внесение наличных на банкомате:'
        self.description = f'{txt_}\n{"-" * len(txt_)}\n' + \
                           f'Клиент {self.client.info()}.\nБанкомат {self.atm.info()}\n' + \
                           f'Операция id={self.id}, сумма={self.src_cash_size}.\n'

        # По условиям банка - налог на богатство 10% вычитается перед
        # каждой операцией, даже ошибочной!
        if self.src_cash_size >= 5000000:
            # зачисляем 10% от операции на счет банкомата для операции > 5млн. у.е.,
            # но не более остатка средств на счете клиента
            self.commision_10_percent_size = self.src_cash_size * 0.1

            self.atm.cash_size += self.commision_10_percent_size
            # сумму операции уменьшаем на 10%
            self.description += 'Внимание!!! По условиям банка - налог на ' \
                                'богатство 10% вычитается перед каждой операцией ' \
                                'на сумму больше 5000000, даже ошибочной!\n' \
                                f'С операции внесения удержан налог 10% в ' \
                                f'сумме {self.commision_10_percent_size}.\n'

        # если операция налогом не облагается, то остаток суммы равен исходной сумме
        self.remain_cash_size = self.src_cash_size - self.commision_10_percent_size

        # вычиcляем размер комиссии в %
        # накладываем доп.условия на размер комиссии:
        # 1. После каждой третей операции пополнения или снятия начисляются проценты - 3%
        if self.atm.oper_count > 0 and self.atm.oper_count % 3 == 0:
            self.commision = 3

        # вычиcляем размер комиссии в у.е.
        self.commision_cash_size = self.remain_cash_size * (self.commision / 100)
        # размер комиссии должен быть не менее 30 и не более 600 у.е.
        if self.commision_cash_size < 30:
            self.commision_cash_size = 30
        elif self.commision_cash_size > 600:
            self.commision_cash_size = 600

        # Проверяем соответствие условиям
        # Сумма пополнения и снятия кратны 50 у.е.
        if self.src_cash_size % 50 != 0:
            # возвращаем деньги клиенту наличными - указав это в сообщении
            self.description += f'Результат: Операция пополнения прервана!\n' \
                                f'Причина: Сумма пополнения должна быть кратна 50 у.е. \n' \
                                f'Клиенту {self.client.fullname} ' \
                                f'возвращено: {self.remain_cash_size}.\n' \
                                f'После операции:\nу клиента: {self.client.account_size}\n' \
                                f'на банкомате: {self.atm.cash_size}.\n'
            return False

        # вычисляем размер суммы зачисления клиенту - отнимаем комиссию от внесенной суммы
        self.clear_cash_size = self.remain_cash_size - \
                               self.commision_cash_size  # commision указываются в процентах!

        # увеличиваем сумму на счете банкомата
        self.atm.cash_size += self.remain_cash_size
        # увеличиваем сумму на счете клиента
        self.client.account_size += self.clear_cash_size

        # Выводим информацию об успешно проведенной операции
        self.description += f'Результат: Операция внесения наличных на счет клиента успешно выполнена.\n' \
                            f'Клиентом {self.client.fullname} внесена сумма: {self.src_cash_size},\n' \
                            f'размер комиссии {self.commision}%, {self.commision_cash_size} (min=30, max=600), ' \
                            f'на его счёт зачислено {self.clear_cash_size}.\n' \
                            f'После операции:\nу клиента: {self.client.account_size}\n' \
                            f'на банкомате: {self.atm.cash_size}.\n'

        self.atm.oper_count += 1

        # записываем в историю операций текущую операцию
        oper_history[len(oper_history) + 1] = History(len(oper_history) + 1, self)

        return True

    def __dispense_cash_to_client(self):
        # выдача наличных банкоматом atm клиенту client.
        # при этом с клиента списывается комиссия в размере commision %

        # размер комиссии по умолчанию
        self.commision = 1.5
        self.description = ''

        # Печатаем предварительную информацию, перед выполнением операции
        txt_ = 'Операция - Выдача наличных банкоматом:'
        self.description = f'{txt_}\n{"-" * len(txt_)}\n' + \
                           f'Клиент {self.client.info()}.\nБанкомат {self.atm.info()}\n' + \
                           f'Операция id={self.id}, сумма={self.src_cash_size}.\n'

        if self.src_cash_size > self.client.account_size:
            self.description += 'Операция прервана, на счету у клиента ' \
                                'недостаточно средств.\n' \
                                f'После операции:\nу клиента: {self.client.account_size}\n' \
                                f'на банкомате: {self.atm.cash_size}.\n'
            return False

        # По условиям банка - налог на богатство 10% вычитается перед
        # каждой операцией, даже ошибочной!
        if self.src_cash_size >= 5000000:
            # зачисляем 10% от операции на счет банкомата для операции > 5млн. у.е.,
            # но не более остатка средств на счете клиента
            self.commision_10_percent_size = self.src_cash_size * 0.1

            # списываем со счета клиента сумму налога 10% от операции
            self.client.account_size -= self.commision_10_percent_size
            # сумму операции уменьшаем на 10%
            self.description += 'Внимание!!! По условиям банка - налог на ' \
                                'богатство 10% вычитается перед каждой операцией ' \
                                'на сумму больше 5000000, даже ошибочной!\n' \
                                f'С операции внесения удержан налог 10% в ' \
                                f'сумме {self.commision_10_percent_size}.\n'

        # если операция налогом не облагается, то остаток суммы равен исходной сумме
        self.remain_cash_size = self.src_cash_size

        # вычиcляем размер комиссии в %
        # накладываем доп.условия на размер комиссии:
        # 1. После каждой третьей операции пополнения или снятия начисляются проценты - 3%
        if self.atm.oper_count > 0 and self.atm.oper_count % 3 == 0:
            self.commision = 3

        # вычиcляем размер комиссии в у.е.
        self.commision_cash_size = self.remain_cash_size * (self.commision / 100)
        # размер комиссии должен быть не менее 30 и не более 600 у.е.
        if self.commision_cash_size < 30:
            self.commision_cash_size = 30
        elif self.commision_cash_size > 600:
            self.commision_cash_size = 600

        # Проверяем соответствие условиям
        # Сумма пополнения и снятия кратны 50 у.е.
        if self.src_cash_size > 0 and self.src_cash_size % 50 != 0:
            # возвращаем деньги клиенту наличными - указав это в сообщении
            self.description += f'Инфо для клиента: Операция прервана!\n' + \
                                f'Сумма снятия должна быть кратна 50 у.е. ' + \
                                f'(сумма операции - {self.src_cash_size})' + \
                                f'После операции:\nна счету клиента: {self.client.account_size}\n' + \
                                f'на банкомате: {self.atm.cash_size}.\n'
            return False

        # Проверяем достаточно ли денег в банкомате для выдачи запрошенной суммы
        if self.src_cash_size > self.atm.cash_size:
            self.description += f'Инфо для клиента: Операция прервана!\n' \
                                f'( денег в банкомате недостачно для выдачи клиенту).\n' \
                                f'После операции:\nу клиента: {self.client.account_size}\n' \
                                f'на банкомате: {self.atm.cash_size}.\n'
            return False

        # увеличиваем сумму на счете банкомата
        self.atm.cash_size -= self.src_cash_size
        # уменьшаем сумму на счете клиента (на банковской карте)
        self.client.account_size -= (self.remain_cash_size + self.commision_cash_size)

        # Выводим информацию об успешно проведенной операции
        self.description += f'Результат: Операция выдачи наличных успешно выполнена.\n' \
                            f'Клиентом {self.client.fullname} ' \
                            f'запрошена сумма: {self.src_cash_size}, ' \
                            f'клиент получил {self.src_cash_size},\n' \
                            f'размер комиссии {self.commision}%, ' \
                            f'{self.commision_cash_size} (min=30, max=600).\n' \
                            f'После операции:\nу клиента: {self.client.account_size}\n' \
                            f'на банкомате: {self.atm.cash_size}.\n'

        self.atm.oper_count += 1

        # записываем в словарь истории операций текущую операцию
        oper_history[len(oper_history) + 1] = History(len(oper_history) + 1, self)

        return True


class History:
    id: int  # идентификатор выполненной операции в истории операций
    oper: Operation
    execute_date: datetime  # дата время выполнения операции

    def __init__(self, id: int, oper: Operation):
        self.id = id
        self.oper = oper
        self.execute_date = datetime.now()  # фиксируем дату/время выполнения операции

    def info(self):
        return f'Запись id: {self.id}, Дата/время совершения операции: {self.execute_date},\n' + \
               f'{self.oper.info()}'


if __name__ == '__main__':
    # Исходные данные
    # словари объектов (словари выбраны для быстрого поиска при обращении к Atm и Client в операции)
    # Банкоматы
    atms = {1: Atm(id=1, adress='г.Москва, ул.Вавилова, 37', cash_size=2000000, oper_count=0),
            2: Atm(id=2, adress='г.Тула, ул.Крылова, 20', cash_size=500000, oper_count=0)}
    # Клиенты
    clients = {1: Client(1, 'Иванов Иван Иванович', 95000),
               2: Client(2, 'Богачев Петр Сергеевич', 10000000),
               3: Client(3, 'Небедный Семен Захарович', 3000)}
    # Список операций, которые будут выполнятся
    operations = \
        [Operation(1, name='внесение', src_cash_size=5000, atm=1, client=1),
         Operation(2, 'внесение', 725, 2, 2),
         Operation(3, 'внесение', 6000000, 2, 3),
         Operation(4, 'снятие', 6000000, 2, 1),
         Operation(5, 'внесение', 20000, 2, 3),
         Operation(6, 'снятие', 45000, 1, 1),
         Operation(7, 'внесение', 3000, 2, 3),
         Operation(8, 'внесение', 10000, 2, 3),
         Operation(9, 'внесение', 100, 2, 3),
         Operation(10, 'снятие', 5000000, 1, 3)]

    # словарь истории выполненных операций (формируется динамически после выполнения операций)
    oper_history = {}

    # Выполнение операций
    txt_ = 'Выполнение операций клиентов на банкоматах'
    print(f'\n   {txt_}\n   {"*" * len(txt_)}\n')

    # выполняем операции
    for oper in operations:
        oper.execute()

    txt_ = 'Архив операций'
    print(f'\n   {txt_}\n   {"*" * len(txt_)}\n')

    # Вывод архива успешно выполненных операций
    for k, h in oper_history.items():
        print(h.info())
