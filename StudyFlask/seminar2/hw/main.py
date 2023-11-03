# Задание
# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя, а также
# будет произведено перенаправление на страницу приветствия, где будет
# отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую
# будет удалён cookie-файл с данными пользователя и произведено перенаправление
# на страницу ввода имени и электронной почты.

from pathlib import PurePath, Path
from flask import Flask, request, render_template, flash, redirect, url_for, session
from werkzeug.utils import secure_filename
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()  # генерация случайного секретного ключа
    #пример значения секретного ключа b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/')
def index():
    if session.get("login", default=None):
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['login'] = request.form.get('login')
        session['email'] = request.form.get('email')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop('login', None)
    session.pop('email', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)