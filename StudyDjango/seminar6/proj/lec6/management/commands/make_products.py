from random import choice, randint, uniform
from django.core.management.base import BaseCommand

from lec5.models import Category, Product

class Command(BaseCommand):
    help = "Generate fake products."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        #очищаем предыдующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        #Добавляем новые данные
        categories = []
        count = kwargs.get('count')
        for i in range(1, 6):
            categories.append(Category(name=f'Категория {i}'))
        Category.objects.bulk_create(categories)  # сохранение списка объектов в БД одной операцией

        categories_all = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
            name=f'продукт номер {i}',
            category=choice(categories_all),
            description='длинное описание продукта, которое и так никто не читает',
            price=uniform(0.01, 999_999.99),
            quantity=randint(1, 10_000),
            rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)  # сохранение списка объектов в БД одной операцией
        print('Данные добавлены в БД.')

# Запуск:
# python manage.py make_products 10000