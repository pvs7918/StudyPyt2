import datetime

from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John',
                        phone="+79996665475",
                        email="123john@gmail.com",
                        full_adress="Moscow",
                        date_registered=datetime.datetime.now())

        client.save()
        self.stdout.write(f'{client}')

# запуск:
# python manage.py create_user