# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


def atm_put_cash_to_account(atm: dict, client: dict, oper: dict):
    # внесение наличных на банкомат atm клиентом client.
    # при этом с клиента списывается комиссия в размере commision %

    # размер комиссии по умолчанию
    oper["commision"] = 1.5

    # Печатаем предварительную информацию, перед выполнением операции
    header_name = 'Операция - Внесение наличных на банкомате:'
    print(header_name + f'\n{"-" * len(header_name)}')
    print('Клиент:')
    print(client)
    print('Банкомат:')
    print(atm)
    print(f'Операция:\nid={oper["id"]}, сумма={oper["src_cash_size"]}.')

    # По условиям банка - налог на богатство 10% вычитается перед
    # каждой операцией, даже ошибочной!
    if oper["src_cash_size"] >= 5000000:
        # зачисляем 10% от операции на счет банкомата для операции > 5млн. у.е.
        atm["cash_size"] += oper["src_cash_size"] * 0.1
        # сумму операции уменьшаем на 10%
        oper["remain_cash_size"] = oper["src_cash_size"] * 0.9
        print('Внимание!!! По условиям банка - налог на богатство 10% вычитается' +
              ' перед каждой операцией на сумму больше 5000000, даже ошибочной!\n' +
        f'С операции внесения удержан налог 10% в сумме {oper["src_cash_size"] * 0.1}.')
    # если операция налогом не облагается, то остаток суммы равен исходной сумме
    else:
        oper["remain_cash_size"] = oper["src_cash_size"]

    # вычиcляем размер комиссии в %
    # накладываем доп.условия на размер комиссии:
    # 1. После каждой третей операции пополнения или снятия начисляются проценты - 3%
    if atm["oper_count"] > 0 and atm["oper_count"] % 3 == 0:
        oper["commision"] = 3

    # вычиcляем размер комиссии в у.е.
    oper["commision_cash_size"] = oper["remain_cash_size"] * (oper["commision"] / 100)
    # размер комиссии должен быть не менее 30 и не более 600 у.е.
    if oper["commision_cash_size"] < 30:
        oper["commision_cash_size"] = 30
    elif oper["commision_cash_size"] > 600:
        oper["commision_cash_size"] = 600

    # Проверяем соответствие условиям
    # Сумма пополнения и снятия кратны 50 у.е.
    if oper["src_cash_size"] % 50 != 0:
        print(f'Инфо для клиента: Операция пополнения прервана!\n' +
              f'Сумма пополнения должна быть кратна 50 у.е. ' +
              f'(получено - {oper["src_cash_size"]})')
        # возвращаем деньги клиенту наличными - указав это в сообщении
        print(f'Клиенту {client["fullname"]} возвращена сумма: {oper["remain_cash_size"]},'
              f'Остаток на счету клиента: {client["account_size"]}')

        print(f'на банкомате {atm["id"]} , остаток средств' +
              f' после операции: {atm["cash_size"]}.\n')
        return False

    # вычисляем размер суммы зачисления клиенту - отнимаем комиссию от внесенной суммы
    oper["clear_cash_size"] = oper["remain_cash_size"] - oper[
        "commision_cash_size"]  # commision указываются в процентах!

    # увеличиваем сумму на счете банкомата
    atm["cash_size"] += oper["src_cash_size"]
    # увеличиваем сумму на счете клиента
    client["account_size"] += oper["clear_cash_size"]

    # Выводим информацию об успешно проведенной операции
    print(f'Операция внесения наличных на счет клиента успешно выполнена.\n'
          f'Клиентом {client["fullname"]} внесена сумма: {oper["src_cash_size"]},'
          f'\n на его счёт зачислено {oper["clear_cash_size"]}, '
          f'размер комиссии {oper["commision"]}%, {oper["commision_cash_size"]} (min=30, max=600).\n'
          f'Остаток на счету клиента: {client["account_size"]}')
    print(f'на банкомате {atm["id"]} внесена сумма: {oper["src_cash_size"]},'
          f'остаток средств после операции: {atm["cash_size"]}.\n')

    atm["oper_count"] += 1
    return True


def atm_dispense_cash_to_client(atm: dict, client: dict, oper: dict):
    # выдача наличных банкоматом atm клиенту client.
    # при этом с клиента списывается комиссия в размере commision %

    # размер комиссии по умолчанию
    oper["commision"] = 1.5

    # Печатаем предварительную информацию, перед выполнением операции
    header_name = 'Операция - Выдача наличных банкоматом:'
    print(header_name + f'\n{"-" * len(header_name)}')
    print('Клиент:')
    print(client)
    print('Банкомат:')
    print(atm)
    print(f'Операция:\nid={oper["id"]}, сумма={oper["src_cash_size"]}.')

    if oper["src_cash_size"] > client["account_size"]:
        print('Операция прервана, на счету у клиента недостаточно средств.\n')
        return False

    # По условиям банка - налог на богатство 10% вычитается перед
    # каждой операцией, даже ошибочной!
    if oper["src_cash_size"] >= 5000000:
        # зачисляем 10% от операции на счет банкомата для операции > 5млн. у.е.,
        # но не более остатка средств на счете клиента
        commision_10_percent_size = oper["src_cash_size"] * 0.1

        atm["cash_size"] += oper["src_cash_size"] * 0.1
        # сумму операции уменьшаем на 10%
        oper["remain_cash_size"] = oper["src_cash_size"] * 0.9
        print('Внимание!!! По условиям банка - налог на богатство 10% вычитается' +
              ' перед каждой операцией на сумму больше 5000000, даже ошибочной!\n' +
              f'С операции внесения удержан налог 10% в сумме {oper["src_cash_size"] * 0.1}.')
    # если операция налогом не облагается, то остаток суммы равен исходной сумме
    else:
        oper["remain_cash_size"] = oper["src_cash_size"]

    # вычиcляем размер комиссии в %
    # накладываем доп.условия на размер комиссии:
    # 1. После каждой третьей операции пополнения или снятия начисляются проценты - 3%
    if atm["oper_count"] > 0 and atm["oper_count"] % 3 == 0:
        oper["commision"] = 3

    # вычиcляем размер комиссии в у.е.
    oper["commision_cash_size"] = oper["remain_cash_size"] * (oper["commision"] / 100)
    # размер комиссии должен быть не менее 30 и не более 600 у.е.
    if oper["commision_cash_size"] < 30:
        oper["commision_cash_size"] = 30
    elif oper["commision_cash_size"] > 600:
        oper["commision_cash_size"] = 600

    # Проверяем соответствие условиям
    # Сумма пополнения и снятия кратны 50 у.е.
    if oper["src_cash_size"] > 0 and oper["src_cash_size"] % 50 != 0:
        print(f'Инфо для клиента: Операция прервана!\n' +
              f'Сумма снятия должна быть кратна 50 у.е. ' +
              f'(сумма операции - {oper["src_cash_size"]})')
        # возвращаем деньги клиенту наличными - указав это в сообщении
        print(f'Остаток на счету клиента: {client["account_size"]}')

        print(f'на банкомате {atm["id"]} , остаток средств' +
              f' после операции: {atm["cash_size"]}.\n')
        return False

    # Проверяем достаточно ли денег в банкомате для выдачи запрошенной суммы
    if oper["src_cash_size"] > atm["cash_size"] :
        print(f'Инфо для клиента: Операция прервана!\n' +
              f'( денег в банкомате недостачно для выдачи клиенту.)')
        print(f'Остаток на счету клиента: {client["account_size"]}, ')
        print(f'на банкомате {atm["id"]} , остаток средств' +
              f' после операции: {atm["cash_size"]}.\n')
        return False

    # вычисляем размер суммы снятия денег клиентом - прибавляем комиссию от внесенной суммы
    oper["clear_cash_size"] = oper["remain_cash_size"] + oper[
        "commision_cash_size"]  # commision указываются в процентах!

    # увеличиваем сумму на счете банкомата
    atm["cash_size"] += oper["clear_cash_size"]
    # уменьаем сумму на счете клиента (на банковской карте)
    client["account_size"] -= oper["clear_cash_size"]

    # Выводим информацию об успешно проведенной операции
    print(f'Операция выдачи наличных со счета клиента успешно выполнена.\n'
          f'Клиентом {client["fullname"]} запрошена сумма: {oper["src_cash_size"]},'
          f'\n клиент получил {oper["src_cash_size"]}, '
          f'размер комиссии {oper["commision"]}%, {oper["commision_cash_size"]} (min=30, max=600).\n'
          f'Остаток на счету клиента: {client["account_size"]}.')
    print(f'Банкоматом {atm["id"]} выдана сумма: {oper["src_cash_size"]},'
          f'остаток средств после операции: {atm["cash_size"]}.\n')

    atm["oper_count"] += 1
    return True


# Исходные данные
# Банкоматы
atms = [{'id': 1, 'cash_size': 2000000, 'adress': 'г.Москва, ул.Вавилова, 37', 'oper_count': 0},
        {'id': 2, 'cash_size': 500000, 'adress': 'г.Тула, ул.Крылова, 20', 'oper_count': 0}]
# Клиенты
clients = [{'id': 1, 'fullname': 'Иванов Иван Иванович', 'account_size': 95000},
           {'id': 2, 'fullname': 'Богачев Петр Сергеевич', 'account_size': 10000000},
           {'id': 3, 'fullname': 'Небедный Семен Захарович', 'account_size': 3000}]
#Операции
operations = \
    [{"src_cash_size": 5000, 'type': 'внесение', "id": 1, 'atm': 1, 'client': 1},
     {"src_cash_size": 725, 'type': 'внесение', "id": 2, 'atm': 2, 'client': 2},
     {"src_cash_size": 6000000, 'type': 'внесение', "id": 3, 'atm': 2, 'client': 3},
     {"src_cash_size": 6000000, 'type': 'снятие', "id": 4, 'atm': 2, 'client': 1},
     {"src_cash_size": 20000, 'type': 'внесение', "id": 5, 'atm': 2, 'client': 3},
     {"src_cash_size": 45000, 'type': 'снятие', "id": 6, 'atm': 1, 'client': 1},
     {"src_cash_size": 3000, 'type': 'внесение', "id": 7, 'atm': 2, 'client': 3},
     {"src_cash_size": 10000, 'type': 'внесение', "id": 8, 'atm': 2, 'client': 3},
     {"src_cash_size": 100, 'type': 'внесение', "id": 9, 'atm': 2, 'client': 3},
     {"src_cash_size": 5000000, 'type': 'снятие', "id": 10, 'atm': 1, 'client': 3}]

# Выполнение операций
print(" Работа банкоматов \n" + '-' * 18 + '\n')

for oper in operations:
    # для операции определяем банкомата и килента по указанным в операции id  - atm, client
    oper_atm = None
    for atm in atms:
        if atm["id"] == oper["atm"]:
            oper_atm = atm

    oper_client = None
    for client in clients:
        if client["id"] == oper["client"]:
            oper_client = client

    if oper["type"].lower() == "внесение":
        atm_put_cash_to_account(oper_atm, oper_client, oper)
    if oper["type"].lower() == "снятие":
        atm_dispense_cash_to_client(oper_atm, oper_client, oper)
