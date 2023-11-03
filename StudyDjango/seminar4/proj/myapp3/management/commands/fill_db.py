import random

from django.core.management.base import BaseCommand
from myapp3.models import Author, Post, Comment

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque blanditiis corporis " \
        "delectus dolores earum incidunt ipsam molestias necessitatibus omnis optio pariatur " \
        "placeat quidem quis quod reiciendis, sed sint sit sunt?"


class Command(BaseCommand):
    help = "Create authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of users')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author{i}', email=f'mail{i}@mail.ru')
            author.save()

            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(random.choices(text, k=64)),
                    author=author,
                    published=random.choice([True, False])
                )
                post.save()
        print('Выполнена команда fill_db.')

# Запуск:
# python manage.py fill_db 10



