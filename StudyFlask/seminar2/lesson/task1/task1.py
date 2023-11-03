# Задание №1
# 📌 Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/hello_world/')
def hello():
    return 'Hello world!'

if __name__ == "__main__":
    app.run(debug=True)