import datetime
import random

from django.core.management.base import BaseCommand
from hw5.models import Client, Category, Product, Order

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # v.1
        Order.objects.all().delete()
        Client.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()

        # v.2
        # orders = Order.objects.all()
        # orders.delete()
        # clients = Client.objects.all()
        # clients.delete()
        # products = Product.objects.all()
        # products.delete()
        # categorys = Category.objects.all()
        # categorys.delete()

        print('Очистка БД завершена.')

# запуск:
# python manage.py clear_db
