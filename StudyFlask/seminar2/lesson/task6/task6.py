# Задание №6
# 📌 Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.
import logging
from pathlib import PurePath, Path

from flask import Flask, request, render_template, flash, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)

logger = logging.getLogger(__name__)

@app.route('/')
@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/hello_world/')
def hello():
    return 'Hello world!'

@app.errorhandler(403)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Доступ запрещен',
        'url': request.base_url
    }
    return render_template('403.html', **context), 403

@app.route('/send/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        if age < 18:
            abort(403)
        return f'Привет, вы успешно вошли в систему'
    return render_template('send.html')

if __name__ == "__main__":
    app.run(debug=True)