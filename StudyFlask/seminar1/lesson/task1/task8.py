# Задание №8
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# 📌 Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.get('/news/')
def news():
    news = [
        {'title': 'С Новым годом!',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'published_at': '01.01.2023'},
        {'title': 'С Днем победы!',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'published_at': '09.05.2023'},
        {'title': 'С Днем программиста!',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'published_at': '13.09.2023'}
    ]
    return render_template('news_task8.html', news=news)    #возвращается шаблон, который должен находится в папке templates проекта

@app.get('/students/')
def students():
    students = [
        {'name': 'Dmitriy',
         'surname': 'Novikov',
         'age': 21,
         'avg_mark': 5.0},
        {'name': 'Stepan',
         'surname': 'Yakovlev',
         'age': 25,
         'avg_mark': 4.0},
        {'name': 'Sidorov',
         'surname': 'Sergey',
         'age': 18,
         'avg_mark': 4.5}
    ]
    return render_template('students_task8.html', students=students)    #возвращается шаблон, который должен находится в папке templates проекта

@app.get('/html/')
def get_simple_html():
    text = """
        <h1>Моя первая html-страница</h1>
        <p>Привет, мир!</p>
    """
    return text

@app.get('/calc/<int:num1>/+/<int:num2>')
def calc_sum(num1, num2):
    summ = num1 + num2
    return f'{num1} + {num2} = {summ}'

@app.get('/')
def hello_world():
    return render_template('hello_task8.html')

@app.get('/about/')
def about():
    return 'About us.'

@app.get('/contacts/')
def contacts():
    return 'My contacts.'

if __name__ == "__main__":
    app.run(debug=True) #debug=True - позволяет вносить изменения в код при запущенном сервере.
                        #Также только в этом режиме видны ошибки в шаблонах.

