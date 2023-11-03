from pydantic import BaseModel, Field
from datetime import date


# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
#   Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия,
#   адрес электронной почты и пароль.
class UserIn(BaseModel):
    name: str = Field(..., min_length=2)
    surname: str = Field(..., min_length=2)
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=6)


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    surname: str = Field(..., min_length=2)
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=6)


# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
#   Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
class ProductIn(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=3)
    price: float = Field(..., gt=0.0)  # указанное значение должно быть больше 0


class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=3)
    price: float = Field(..., gt=0.0)  # указанное значение должно быть больше 0


# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
#   Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY),
#   id товара (FOREIGN KEY), дата заказа и статус заказа.
class OrderIn(BaseModel):
    user_id: int = Field(..., gt=0)
    product_id: int = Field(..., gt=0)
    order_date: date = Field(..., format="%Y-%m-%d")
    status: str = Field(..., min_length=1)


class Order(BaseModel):
    id: int
    user_id: int = Field(..., gt=0)
    product_id: int = Field(..., gt=0)
    order_date: date = Field(..., format="%Y-%m-%d")
    status: str = Field(..., min_length=1)
