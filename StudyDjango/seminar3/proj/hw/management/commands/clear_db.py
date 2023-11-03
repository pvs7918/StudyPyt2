import datetime
import random

from django.core.management.base import BaseCommand
from hw.models import Client, Product, Order


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        orders = Order.objects.all()
        orders.delete()

        clients = Client.objects.all()
        clients.delete()

        products = Product.objects.all()
        products.delete()

        print('Очистка БД завершена.')

# запуск:
# python manage.py clear_db
