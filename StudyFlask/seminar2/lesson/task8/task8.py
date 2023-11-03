# Задание №8
# 📌 Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from pathlib import PurePath, Path

from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import secrets

secrets.token_hex()


app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/')
@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/hello_world/')
def hello():
    return 'Hello world!'

@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('html_index'))


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)