# В этом примере определены три модели данных: Item, User и Order. Каждая модель
# данных содержит поля с указанными для них типами. Поле is_offer в модели Item
# имеет значение по умолчанию None.


from typing import List
from fastapi import FastAPI

# Field импортируется непосредственно из pydantic, а не из
# fastapi как для всех остальных (Query, Path и т.д.).
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


class User(BaseModel):
    # Функция Field позволяет задавать различные параметры для поля, такие как тип
    # данных, значение по умолчанию, ограничения на значения и т.д. Например, чтобы
    # задать поле типа str с ограничением на длину в 10 символов
    username: str = Field(max_length=10)
    full_name: str = None
    # Еще один пример использования функции Field — это задание значения по умолчанию
    # для поля.Например, чтобы задать поле типа int со значением по умолчанию 0, можно
    # использовать следующий код:
    age: int = Field(default=0)


class Order(BaseModel):
    items: List[Item]
    user: User
