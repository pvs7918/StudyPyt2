from django.db import models
from django.utils import timezone


# Модель Клиент
class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    full_adress = models.CharField(max_length=150)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Клиент id: {self.pk}, имя: {self.name}, телефон: {self.phone}.'


# Модель Категория (товара)
class Category(models.Model):
    name = models.CharField(default='', max_length=50, unique=True)

    def __str__(self):
        return self.name


# Модель Товар
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    description = models.TextField(default='', blank=True)
    price = models.FloatField(default=999999.99)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    rating = models.DecimalField(default=5.0, max_digits=3,
                                 decimal_places=2)
    foto = models.ImageField(blank=True)

    def __str__(self):
        return f'Товар id: {self.pk}, имя: {self.name}, цена={self.price}.'

    def __repr__(self):
        return f'Товар id: {self.pk}, имя: {self.name}, описание: {self.description},\n' \
               f'цена: {self.price}, кол-во: {self.quantity}, дата добавления: {self.date_added}.'


# модель «Заказ»:
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_summ = models.FloatField(default=0)
    date_ordered = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'\nЗаказ id: {self.pk}, клиент: {self.client.name}.'

    def __repr__(self):
        return f'\nЗаказ id: {self.pk}, клиент: {self.client}, ' \
               f'дата заказа: {self.date_ordered},\nтовары: {self.products.all()}.\n'
