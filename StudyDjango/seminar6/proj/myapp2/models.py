from django.db import models
from django.utils import timezone


# Задание №1
# 📌 Создайте модель для запоминания бросков монеты: орёл или
# решка.
# 📌 Также запоминайте время броска

class SaveCoin(models.Model):
    coin = (('О', 'Орел'), ('Р', 'Решка'))
    coin_variant = models.CharField(max_length=1, choices=coin)
    date = models.DateTimeField(default=timezone.now)

    @staticmethod
    def statistics(n):
        return SaveCoin.objects.all()


# Создайте три модели Django: клиент, товар и заказ.
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    full_adress = models.CharField(max_length=150)
    date_registered = models.DateTimeField()

    def __str__(self):
        return f'Client id: {self.id}, name: {self.name}, phone: {self.phone}'

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField
    price = models.FloatField
    quantity = models.IntegerField
    date_added = models.DateTimeField()

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    products_ids = models.ForeignKey(Product, on_delete=models.CASCADE)
    summ = models.FloatField
    date_ordered = models.DateTimeField()