# Задание №2
# 📌 Создать базу данных для хранения информации о книгах в библиотеке.
# 📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
# 📌 В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# 📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# 📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
# 📌 Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template, request, url_for, redirect, make_response, flash
from models import db, User
from forms import RegistrationForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
db.init_app(app)
csrf = CSRFProtect(app)

# чтобы запустить в командной строке дать команду: flask init-db
# в каталоге проекта должен быть файл wsgi.py
# запуск в командной строке из пути проекта
# после выполнения, файл БД появится в проекте в подкаталоге instance
# работать с файлом SQLite можно с помощью DBeaver, SQLite Studio
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('init-db OK')



@app.route('/')
def home():
    users = User.query.all()
    context = {'users': users}
    return render_template('home.html', **context)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User (
            full_name=form.full_name.data,
            e_mail=form.e_mail.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()

        response = make_response(redirect(url_for('home')))
        flash('Регистрация выполнена успешно!', 'success')
        return response

    return render_template('register.html', form=form)



# Запуск
# В Терминале находясь в каталоге проекта task2 запукаем команды
# flask init-db
# Далее запускаем на выполнение файл wsgi.py
