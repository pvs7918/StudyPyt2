# Задание №4
# 📌 Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# 📌 При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

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

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num1'))
    oper = int(request.form.get('operation'))
    if oper == 'add':
        return f'{num1 + num2}'
    if oper == 'substract':
        return f'{num1 - num2}'
    if oper == 'multiply':
        return f'{num1 * num2}'
    if oper == 'divide':
        return f'{num1 / num2}'
    return render_template('calc.html')


if __name__ == "__main__":
    app.run(debug=True)