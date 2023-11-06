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

    def __str__(self):
        return f'-{self.coin_variant}-  '

    @staticmethod
    def statistics(n):
        return SaveCoin.objects.all()[:n]

    class Meta:
        ordering = ["-date"]


class Product(models.Model):
    name = models.CharField(max_length=50)

    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8,
                                decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    rating = models.DecimalField(default=5.0, max_digits=3,
                                 decimal_places=2)

    def __str__(self):
        return self.name
