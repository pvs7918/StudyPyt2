# Задание
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль"
# и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных,
# а пароль должен быть зашифрован.


from flask import Flask, render_template, request, url_for, redirect, make_response, flash
from models import db, User
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session

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
            name=form.name.data,
            surname=form.surname.data,
            e_mail=form.e_mail.data,
            pwd_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()

        response = make_response(redirect(url_for('home')))
        flash('Регистрация пользователя выполнена успешно!', 'success')
        return response

    return render_template('register.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate():
        if User.query.filter(User.e_mail == form.e_mail.data).count() == 1:
            user = User.query.filter(User.e_mail == form.e_mail.data).first()
            if check_password_hash(user.pwd_hash, form.password.data):
                return render_template('welcome.html', user=user)
        flash('Такой пользователь не зарегистрирован!', "danger")
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout/')
def logout():
    return redirect(url_for('home'))

# Запуск
# В Терминале находясь в каталоге проекта task2 запуcкаем команды
# flask init-db
# Далее запускаем на выполнение файл wsgi.py
