from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from hw.models import Client, Product, Order
from datetime import date, timedelta
import datetime


# Домашняя работа
# Задание
# Продолжаем работать с товарами и заказами.
# 📌 Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.

#
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
# Товары в списке не должны повторятся.

# сначала БД была наполнена с помощью написанных команд:
# python manage.py clear_db  #очистка БД, если что-то пошло не так.
# python manage.py add_data_to_db

def index(request):
    return render(request, 'hw/index.html')


def clients(request):
    clients = Client.objects.all()
    return render(request, 'hw/clients.html',
                  {'clients': clients})


def client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'hw/client.html',
                  {'client': client})


def products(request):
    products = Product.objects.all()
    return render(request, 'hw/products.html',
                  {'products': products})


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'hw/product.html',
                  {'product': product})


def orders(request):
    orders_list = Order.objects.all()    #date_ordered
    return render(request, 'hw/orders.html',
                  {'orders': orders_list})


def orders_for_days(request, days_cnt):
    orders_list = Order.objects.filter(
        date_ordered__gt=date.today() - datetime.timedelta(days=days_cnt)).order_by('-date_ordered')
    return render(request, 'hw/orders.html',
                  {'orders': orders_list})


# 📌 Создайте шаблон для вывода всех заказов клиента и
# списком товаров внутри каждого заказа.
# 📌 Подготовьте необходимый маршрут и представление.

def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'hw/client_orders.html',
                  {'client': client,
                   'orders': orders
                   })


# вывод всех товаров заказа
def order_products(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = Product.objects.filter(order=order)
    return render(request, 'hw/order_products.html',
                  {'order': order,
                   'products': products
                   })

