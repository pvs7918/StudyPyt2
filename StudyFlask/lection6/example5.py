# Создание API операций CRUD
# Обсудим, как создать API операций CRUD (создание, чтение, обновление и
# удаление) с использованием FastAPI и SQLAlchemy ORM.
# Операции CRUD — это основные функции, которые используются в любом
# приложении, управляемом базой данных. Они используются для создания, чтения,
# обновления и удаления данных из базы данных. В FastAPI с SQLAlchemy ORM мы
# можем создавать эти операции, используя функции и методы Python.
# ● CREATE, Создать: добавление новых записей в базу данных.
# ● READ, Чтение: получение записей из базы данных.
# ● UPDATE, Обновление: изменение существующих записей в базе данных.
# ● DELETE, Удалить: удаление записей из базы данных.

# Работа с БД в CRUD операциях с SQLAlchemy и databases

# Для работы с базой данных в операциях CRUD с SQLAlchemy ORM нам необходимо
# сначала установить соединение с базой данных. Мы можем использовать любую
# базу данных по нашему выбору, такую как MySQL, PostgreSQL или SQLite. После того,
# как мы установили соединение, мы можем выполнять операции CRUD в базе
# данных, используя SQLAlchemy ORM.
# Например, предположим, что у нас есть база данных SQLite, в которой мы создадим
# таблицу под названием «пользователи». Мы можем подключиться к базе данных,
# используя следующий код:
from typing import List

import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


# Создание моделей для взаимодействия с таблицей в БД
# Создадим две модели данных Pydantic:

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# Первая модель нужна для получения информации о пользователе от клиента. А
# вторая используется для возврата данных о пользователе из БД клиенту.
# Добавление тестовых пользователей в БД
# Прежде чем работать над созданием API и проходить всю цепочку CRUD для
# клиента сгенерируем несколько тестовых пользователей в базе данных.


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}',
                                      email=f'mail{i}@mail.ru')
        await database.execute(query)
    return {'message': f'{count} fake users created'}


# Принимаем целое число count и создаём в БД указанное число пользователей с
# именами и почтами. Теперь мы готовы не только разрабатывать CRUD, но и
# тестировать его.

# После запуска перейти по адресу http://127.0.0.1:8000/fake_users/25
# чтобы добавить пользователей


# Формирование CRUD

# Создадим необходимые маршруты для реализации REST API.
# Чтобы создать нового пользователя в таблице «users», мы можем определить
# функцию следующим образом:

# ➢ Создание пользователя в БД, Create
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}
# Мы определяем маршрут "/users/" для создания нового пользователя. В параметре
# функции мы ожидаем объект типа UserIn, который содержит имя и email
# пользователя. Затем мы создаем SQL-запрос на добавление новой записи в таблицу
# "users" с указанными данными. Выполняем запрос и возвращаем данные
# созданного пользователя, включая его ID.


# Чтобы прочитать всех пользователей из таблицы «users», мы можем определить
# функцию следующим образом:

# ➢ Чтение всех пользователей из БД, read
@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)
# Мы определяем маршрут "/users/" для чтения всех пользователей. В функции мы
# создаем SQL-запрос на выборку всех записей из таблицы "users". Выполняем запрос
# и возвращаем полученные данные в виде списка объектов типа User.

# Чтобы прочитать одного пользователей из таблицы «users», мы можем определить
# функцию следующим образом:
#
# ➢ Чтение одного пользователя из БД, read
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)
# Мы определяем маршрут "/users/{user_id}" для чтения одного пользователя по его
# ID. В параметре функции мы ожидаем передачу ID пользователя. Затем мы создаем
# SQL-запрос на выборку записи из таблицы "users" с указанным ID. Выполняем
# запрос и возвращаем полученные данные в виде объекта типа User.


# Чтобы обновить данные пользователя в таблице «users», мы можем определить
# функцию следующим образом:

# ➢ Обновление пользователя в БД, update

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}
# Мы определяем маршрут "/users/{user_id}" для обновления данных пользователя по
# его ID. В параметре функции мы ожидаем передачу ID пользователя и объекта типа
# UserIn, который содержит новые данные пользователя. Затем мы создаем
# SQL-запрос на обновление записи в таблице "users" с указанным ID и новыми
# данными. Выполняем запрос и возвращаем обновленные данные пользователя.


# Чтобы удалить пользователя из таблицы «users», мы можем определить функцию
# следующим образом:

# ➢ Удаление пользователя из БД, delete

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
# Мы определяем маршрут "/users/{user_id}" для удаления пользователя по его ID. В
# параметре функции мы ожидаем передачу ID пользователя. Затем мы создаем
# SQL-запрос на удаление записи из таблицы "users" с указанным ID. Выполняем
# запрос и возвращаем сообщение об успешном удалении пользователя.

# Тестирование операций CRUD
# Чтобы протестировать наш API операций CRUD, мы можем использовать такие
# инструменты, как Postman или Swagger UI. Мы можем отправлять HTTP-запросы к
# нашему API и проверять правильность создания, чтения, обновления и удаления
# данных.
# Мы можем использовать интерактивную документацию или curl для проверки этих
# конечных точек, отправляя HTTP-запросы с соответствующими параметрами.
# Например, чтобы создать нового пользователя, мы можем отправить запрос POST
# на конечную точку « /users » с данными пользователя в теле запроса.
# curl -X 'POST' \
# 'http://127.0.0.1:8000/users/' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
# "name": "Alex",
# "email": "my@mail.ru"
# }'
# Затем мы можем убедиться, что пользователь был создан в базе данных, отправив
# запрос GET на конечную точку « /users » и проверив, что пользователь присутствует
# в ответе.
# Создание API операций CRUD в FastAPI - это простой процесс. Мы можем
# использовать функции и методы Python для выполнения основных функций
# создания, чтения, обновления и удаления данных из базы данных. Мы можем
# протестировать наш API с помощью таких инструментов, как Postman или Swagger (через http://127.0.0.1:8000/docs)
# UI, чтобы убедиться, что он работает правильно.

# проверл успешное тестирование. Сначала запустил этот модуль
# Затем запустил Swagger в браузере перешел по адресу: http://127.0.0.1:8000/docs
# там протестировал все запросы. В режиме отправил запрос посмотрел ответ

#Запуск сервера. example5 - название этого моудля Python
if __name__ == '__main__':
    uvicorn.run(
        "example5:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
