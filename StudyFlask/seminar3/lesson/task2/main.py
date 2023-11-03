# Задание №2
# 📌 Создать базу данных для хранения информации о книгах в библиотеке.
# 📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
# 📌 В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# 📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# 📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
# 📌 Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template
from models import db, Book, Author, AuthorBook

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

# чтобы запустить в командной строке дать команду: flask init-db
# в каталоге проекта должен быть файл wsgi.py
# запуск в командной строке из пути проекта
# после выполнения, файл БД появится в проекте в подкаталоге instance
# работать с файлом SQLite можно с помощью DBeaver, SQLite Studio
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('init-db OK')


# наполнение БД тестовыми данными
# для запуска набрать в терминале команду: flask fill-db
@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем книги
    for number in range(1, count + 1):
        book = Book(title=f'book_{number}', published_year=1997+number, copy_count=1+number)
        db.session.add(book)
        db.session.commit()

        # Добавляем авторов
        for number in range(1, count+1):
            author = Author(
                name=f'name_{number}',
                surname=f'surname_{number}',
            )
            db.session.add(author)
            db.session.commit()

    db.session.add(AuthorBook(author_id=1, book_id=1))
    db.session.add(AuthorBook(author_id=2, book_id=1))

    db.session.add(AuthorBook(author_id=2, book_id=2))
    db.session.add(AuthorBook(author_id=3, book_id=2))
    db.session.add(AuthorBook(author_id=4, book_id=2))

    db.session.add(AuthorBook(author_id=5, book_id=3))
    db.session.add(AuthorBook(author_id=1, book_id=4))
    db.session.add(AuthorBook(author_id=2, book_id=5))
    db.session.commit()

    print('fill-db OK')


@app.route('/')
def all_users():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


# Запуск
# В Терминале находясь в каталоге проекта task2 запукаем команды
# flask init-db
# flask fill-db
# Далее запускаем на выполнение файл wsgi.py
