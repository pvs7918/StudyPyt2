# Задание №3
# 📌 Создать страницу, на которой будет форма для ввода логина
# и пароля.
# 📌 При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

from pathlib import PurePath, Path

from flask import Flask, request, render_template, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/hello_world/')
def hello():
    return 'Hello world!'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))  # папку uploads нужно создать в проекте
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')

user = {
    "Login": "Ivan",
    "Password": "123"
}

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == user['Login'] and password == user['Password']:
            return f'Привет {login}!'
    else:
        flash('Логин или пароль неверные')
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)