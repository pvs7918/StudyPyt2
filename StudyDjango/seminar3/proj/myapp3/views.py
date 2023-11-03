import random

from django.shortcuts import render, get_object_or_404
from myapp3.models import Author, Post, Comment


def index(request):
    return render(request, 'myapp3/index.html')


def about(request):
    return render(request, 'myapp3/about.html')


# Задание №3
# 📌 Доработаем задачу 7 из урока 1, где бросали монетку,
# игральную кость и генерировали случайное число.
# 📌 Маршруты могут принимать целое число - количество
# бросков.
# 📌 Представления создают список с результатами бросков и
# передают его в контекст шаблона.
# 📌 Необходимо создать универсальный шаблон для вывода
# результатов любого из трёх представлений.

def coin(request, count):
    coins = []
    for i in range(1, count + 1):
        cur_coin = random.choice(["Орел", "Решка"])
        coins.append(cur_coin)
    return render(request, 'myapp3/result_game.html',
                  {
                      'result': coins,
                      'game': 'сторона монеты - '
                  })


def cube(request, count):
    res_list = []
    for i in range(1, count + 1):
        attemp = random.randint(1, 7)
        res_list.append(attemp)

    return render(request, 'myapp3/result_game.html',
                  {
                      'result': res_list,
                      'game': 'сторона куба - '
                  })


def number_random(request, count):
    numbers = (str(random.randint(0, 101)))
    return render(request, 'myapp3/result_game.html',
                  {
                      'result': numbers,
                      'game': 'сторона монеты - '
                  })


# Задание №4
# 📌 Доработаем задачи из прошлого семинара по созданию
# моделей автора, статьи и комментария.
# 📌 Создайте шаблон для вывода всех статей автора в виде
# списка заголовков.
# ○ Если статья опубликована, заголовок должен быть
# ссылкой на статью.
# ○ Если не опубликована, без ссылки.
# 📌 Не забываем про код представления с запросом к базе
# данных и маршруты.

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'myapp3/author_posts.html',
                  {'author': author,
                   'posts': posts
                   })


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_view.html',
                  {'post': post}
                  )

