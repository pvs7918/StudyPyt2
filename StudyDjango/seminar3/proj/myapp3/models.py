from django.db import models
from django.utils import timezone


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

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        if self.id:
            return f'Name: name: {self.name}, email: {self.email}'
        return 'None'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.BooleanField()

    def __str__(self):
        if self.id:
            return f'Title is {self.title}'


class Comment(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.id:
            return f'Comment {self.comment}, date = {self.date}'
        return 'None'
