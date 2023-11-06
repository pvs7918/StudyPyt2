import datetime
import random

from django.core.management.base import BaseCommand
from hw5.models import Client, Category, Product, Order
from datetime import date, timedelta
import os


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        days_before = 500  # сколько дней назад от текущей даты для случайной генерации (нужно для фильтрации по дате добалвения товара, 7, 30, 365 дней)

        # предварительно запускаем команду очистки БД
        os.system("python manage.py clear_db")

        categories = []
        for i in range(1, 6):
            category = Category(name=f'Category{i}')
            # category.save()
            categories.append(category)  # в список добавляем id (pk) продукта
        print(f"Добавлено {len(categories)} категорий.\n")
        Category.objects.bulk_create(categories) # v2 групповое добавление объектов

        products = []
        for i in range(1, 11):
            product = Product(name=f'Product{i}',
                              category=random.choice(Category.objects.all()),
                              description=f'description{i}',
                              price=round(random.uniform(10, 1000), 2),
                              quantity=random.randint(1, 100),
                              date_added=date.today() - datetime.timedelta(days=random.randint(0, days_before)))

            # product.save()
            products.append(product)  # в список добавляем id (pk) продукта
        Product.objects.bulk_create(products) # v2 групповое добавление объектов


        print(f"Добавлено {len(products)} продуктов.\n{products=}")
        clients = []
        for i in range(1, 11):
            client = Client(name=f'Client{i}',
                            phone=f"+79{random.randint(100000000, 1000000000)}",
                            email=f"client{i}@mail.ru",
                            full_adress=f"{i}-я улица, {random.randint(1, 150)}-{random.randint(1, 51)}",
                            date_registered=date.today() - datetime.timedelta(days=random.randint(0, days_before)))

            # client.save()
            clients.append(client)  # в список добавляем id (pk) клиента
        Client.objects.bulk_create(clients)
        print(f"Добавлено {len(clients)} клиентов.\n{clients=}")

        orders = []
        # создаем заказы cметодом create, и только потом добавляем связанные записи типа ManyToMany
        # потому что надо чтобы предварительно чтобы появился у заказа id (pk)

        for j in range(51):
            order = Order.objects.create(
                client=random.choice(Client.objects.all()),
                date_ordered=date.today() - datetime.timedelta(days=random.randint(0, days_before))
            )
            # # добавляем в заказ продукты
            #   вариант 1 - добавление списком
            #     selected_products = Product.objects.filter(id__in=random.choices(products, k=4))
            #     order.products.set(selected_products)
            #   вариант 2 - добавление по одному
            cur_summ = 0.0
            k = random.randint(2, 4)
            for k in range(k): #колиство товаор в заказе случайно от 2 до 5
                cur_product = random.choice(Product.objects.all())
                order.products.add(cur_product)
                cur_summ += cur_product.price  # вычисляем сумму заказа
            order.order_summ = round(cur_summ, 2)
            order.save()  # это обязательно после обновления полей. Проверено опытным путем
            orders.append(order)

        print(f"Заказы\n{orders}.")
        print("Заказы добавлены.")

        print("Выполнено add_data_to_db.")
#
# запуск:
# python manage.py add_data_to_db
