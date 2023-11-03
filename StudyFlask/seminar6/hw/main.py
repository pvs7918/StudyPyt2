# Необходимо создать базу данных для интернет-магазина. База данных должна состоять
# из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия,
#   адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY),
#   id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
#
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой
# из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.
import random
import string
from datetime import date, timedelta

import uvicorn
from db import database, tbl_users, tbl_products, tbl_orders
from fastapi import FastAPI

import users
import orders
import products

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router, tags=["users"])
app.include_router(products.router, tags=["products"])
app.include_router(orders.router, tags=["orders"])


# Добавление тестовых данных. Подробности в конце данного модуля
@app.get("/fill_db/")
async def create_test_data():
    # Добавление пользователей - 5 чел.
    for i in range(1, 6):
        query = tbl_users.insert().values(name=f'test_user_{i}',
                                          surname=f'surname {i}',
                                          email=f'user{i}@test.com',
                                          password=random.randint(1, 1000000))
        await database.execute(query)

    # Добавление продуктов - 5 шт.
    for i in range(1, 6):
        query = tbl_products.insert().values(name=f'test_user_{i}',
                                             description=''.join(
                                                 random.choices(string.ascii_letters, k=15)),
                                             price=round(random.uniform(10.0, 1000.0), 1)
                                             )
        await database.execute(query)

    # добавление заказов - 10шт.
    for i in range(1, 11):
        query = tbl_orders.insert().values(user_id=random.randint(1, 6),
                                           product_id=random.randint(1, 6),
                                           order_date=date.today() - timedelta(days=random.randint(0, 365)),
                                           status=random.choice(['выполняется', 'завершен', 'отменён'])
                                           )
        await database.execute(query)

    return {'message': 'test data successfully added to DB.'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# Инструкция:
# 1. Создайте БД запустив данный модуль main.py
# 2. Добавьте тестовые данные выполнив в браузере: http://127.0.0.1:8000/fill_db/
# 3. Проверка наличия данных и тестирование CRUD операций лучше выполнить
#    через Swager по адресу: http://127.0.0.1:8000/docs
