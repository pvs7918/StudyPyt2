from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    full_adress = models.CharField(max_length=150)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Client id: {self.pk}, name: {self.name}, phone: {self.phone}.'

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Product id: {self.pk}, name: {self.name}, descr: {self.description},\n' \
               f'price: {self.price}, quantity: {self.quantity}, date_added: {self.date_added}.'

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_summ = models.FloatField(default=0)
    date_ordered = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'\nOrder id: {self.pk}, client: {self.client}, order_summ: {self.order_summ},' \
               f'date_ordered: {self.date_ordered},\nproducts: {self.products.all()}.\n'
