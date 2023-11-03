# Задание №2
# 📌 Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.
from pathlib import PurePath, Path

from flask import Flask, request, render_template
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

if __name__ == "__main__":
    app.run(debug=True)