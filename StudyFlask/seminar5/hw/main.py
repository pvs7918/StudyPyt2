# Задание
# Необходимо создать API для управления списком пользователей.
# Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# — GET /users — возвращает список всех пользователей.
# — GET /users/{id} — возвращает пользователя с указанным идентификатором.
# — POST /users — добавляет нового пользователя.
# — PUT /users/{id} — обновляет пользователя с указанным идентификатором.
# — DELETE /users/{id} — удаляет пользователя с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.

# требуется установка python-multipart:
# pip install python-multipart

import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from flask import render_template
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Для валидации данных класс наследуется от класса BaseModel.
# Это позволит валидировать поля в  запросах и ответах.
# Если данные не соответствуют описанию класса Item,
# то FastAPI вернет ошибку 422 с описанием ошибки.
class UserAttrs(BaseModel):
    name: str
    email: str

class User(UserAttrs):
    id: int

collection = [
    User(id=1, name='Viktorov Aleksandr', email='viktorov@mail.tu'),
    User(id=2, name='Dyakov Semen', email='dyakov2@first.su')
]


#получить список всех пользователей
@app.get('/users/', response_class=HTMLResponse)
def users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": collection})

#получить пользователя с нужным id
@app.get('/users/{id}', response_class=HTMLResponse)
def user_get_by_id(request: Request, id: int):
    for user in collection:
        if user.id == id:
            return templates.TemplateResponse("users.html", {"request": request, "users": [user]})
        raise HTTPException(status_code=404, detail="User not found")

# POST - добавление пользователя
@app.post('/users/', response_class=HTMLResponse)
def create_user(request: Request, name: Annotated[str, Form()], email: Annotated[str, Form()]):
    user = User(id=len(collection) + 1, email=email, name=name)
    collection.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "users": collection})

# PUT(id) - обновление пользователя
@app.put('/users/', response_class=HTMLResponse)
def update_user(request: Request, attrs: UserAttrs):
    for user in collection:
        if user.id == attrs.id2:
            user.name = attrs.name2
            user.email = attrs.email2
            return templates.TemplateResponse("users.html", {"request": request, "users": collection})
    raise HTTPException(status_code=404, detail="User not found")

#DELETE(id) - удаление пользователя
@app.delete('/users/{id}', response_model=HTMLResponse)
def delete_user(request: Request, id: int):
    for user in collection:
        if user.id == id:
            collection.remove(user)
        return templates.TemplateResponse("users.html", {"request": request, "users": collection})
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
