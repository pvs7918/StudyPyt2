# А чтобы получить пользователя по его ID, мы можем использовать следующий
# код в файле myapp2/management/commands/get_user.py:

from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        # pk в Django заменяет id. так есть встроенный метод id()
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')

# Метод add_arguments позволяет парсить командную строку.
# Мы получаем значение целого типа и сохраняем его по ключу id. Теперь обработчик
# handler # может получить к идентификатору доступ через ключ словаря kwargs.

# Запустим команду:

# python manage.py get_user 10
# None
# python manage.py get_user 4
# Username: id: 4, name: John, email: john@example.com, age: 25



