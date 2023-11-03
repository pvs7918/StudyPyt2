# Домашнее задание
# 📌 Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.get('/clothes/')
def clothes_show():
    clothes_list = [
        {'title': 'Майка спортивная',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'size': 'XL',
         'price': 2000.0},
        {'title': 'Джинсы синие Wrangler',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'size': 'XXL',
         'price': 5000.0},
        {'title': 'Кепка летняя Nike',
         'description': ' Nike - Lorem ipsum dolor sit amet',
         'size': 'M',
         'price': 1500.0}
    ]
    return render_template('clothes.html', data=clothes_list)    #возвращается шаблон, который должен находится в папке templates проекта

@app.get('/shoes/')
def shoes_show():
    shoes_list = [
        {'title': 'Кроссовки Asics Gel-Excite 9',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'size': '44',
         'price': 6350.0},
        {'title': 'Туфли женские',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'size': '35 - 38',
         'price': 5000.0},
        {'title': 'Ботильоны женские демисезонные на каблуке',
         'description': 'Aliquid cumque est id nam nisi nobis similique temporibus velit.',
         'size': '36, 38, 39',
         'price': 2730.0},
        {'title': 'Лоферы женские',
         'description': ' Nike - Lorem ipsum dolor sit amet',
         'size': '35, 36, 37',
         'price': 3400.0},
        {'title': 'Ботинки кожаные зимние',
         'description': 'Adipisci aperiam blanditiis ducimus eaque modi provident, recusandae reprehenderit veritatis.',
         'size': '41 - 45',
         'price': 6200.0}
    ]
    return render_template('shoes.html', data=shoes_list)    #возвращается шаблон, который должен находится в папке templates проекта

@app.get('/jackets/')
def jackets_show():
    jackets_list = [
        {'title': 'куртка мужская зимняя с капюшоном длинная',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'size': 'L, XL',
         'price': 10499.0},
        {'title': 'Косуха женская кожаная',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, ad.',
         'size': 'M, L',
         'price': 4299.0},
        {'title': 'Пуховик зимний длинный',
         'description': 'Aliquid cumque est id nam nisi nobis similique temporibus velit.',
         'size': '44, 46, 48',
         'price': 12099.0}
    ]
    return render_template('jackets.html', data=jackets_list)    #возвращается шаблон, который должен находится в папке templates проекта




@app.get('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) #debug=True - позволяет вносить изменения в код при запущенном сервере.
                        #Также только в этом режиме видны ошибки в шаблонах.

