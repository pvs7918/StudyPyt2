import random

from django.shortcuts import render
from .forms import GameForm

import logging

from .models import Author, Post

logger = logging.getLogger(__name__)


# Задание №1
# 📌 Доработаем задачу про броски монеты, игральной кости и
# случайного числа.
# 📌 Создайте форму, которая предлагает выбрать: монета, кости,
# числа.
# 📌 Второе поле предлагает указать количество попыток от 1 до 64.

def coin(request, count):
    coins = []
    for i in range(1, count + 1):
        cur_coin = random.choice(["Орел", "Решка"])
        coins.append(cur_coin)
    return render(request, 'sem4/result_game.html',
                  {
                      'result': coins,
                      'game': 'сторона монеты - '
                  })


def cube(request, count):
    res_list = []
    for i in range(1, count + 1):
        attemp = random.randint(1, 7)
        res_list.append(attemp)

    return render(request, 'sem4/result_game.html',
                  {
                      'result': res_list,
                      'game': 'сторона куба - '
                  })


def number_random(request, count):
    numbers = (str(random.randint(0, 101)))
    return render(request, 'sem4/result_game.html',
                  {
                      'result': numbers,
                      'game': 'сторона монеты - '
                  })


# Задание №2
# 📌 Доработаем задачу 1.
# 📌 Создайте представление, которое выводит форму выбора.
# 📌 В зависимости от переданных значений представление
# вызывает одно из трёх представлений, созданных на
# прошлом семинаре (если данные прошли проверку, конечно
# же).

def form_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)  # создаем форму с переданными данными
        if form.is_valid():
            # Если форма проходит валидацию(все поля заполнены корректно), то мы получаем данные
            # из формы и можем с ними работать.
            game = form.data['selected_game']
            quantity = form.data['quantity']
            # Делаем что-то с данными
            logger.info(f'Получили {game=}, {quantity=}.')

            if game == 'coin':
                return coin(request, quantity)
            if game == 'cube':
                return cube(request, quantity)
            if game == 'number_random':
                return number_random(request, quantity)
    else:
        # Если запрос пришел методом GET, то мы просто создаем пустой экземпляр формы UserForm
        # и передаем его в шаблон user_form.html.
        form = GameForm()
        # В шаблоне user_form.html мы можем вывести нашу форму с помощью тега {{form}}.
        message = 'Заполните форму'
        return render(request, 'sem4/form_game.html',
                      {'form': form, 'message': message})



# Задание №4
# 📌 Аналогично автору создайте форму добавления новой статьи.
# 📌 Автор статьи должен выбираться из списка (все доступные в базе данных авторы).

# def add_author(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             name = form.data['name']
#             email = form.data['email']
#             author = Author(name=name, email=email)
#             author.save()
#             return render(request, 'sem4/result.html')
#     else:
#         form = AuthorForm()
#         return render(request, 'sem4/add_author.html', {'form': form})


# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             title = form.data['title']
#             content = form.data['content']
#             author = form.data['author']
#             post = Post(title=title,content=content,author=author)
#             post.save()
#             return render(request, 'sem4/result.html')
#     else:
#         form = PostForm()
#         return render(request, 'sem4/add_post.html', {'form': form})