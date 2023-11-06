from django.shortcuts import render
from django.db.models import Sum
from lec5.models import Product

# Метод aggregate(Sum('quantity')) отправит в базу агрегирующий запрос с
# суммированием всех значений столбца “количество”. Результат пробрасывается в
# шаблон total_count.html как параметр total.
def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'lec6/total_count.html', context)

# Во втором случае возложим задачу по подсчёту общего количества продуктов на
# само представление:
# Метод all возвращает все продукты из базы данных. Далее в цикле перебираем
# продукты и функция sum подсчитывает результат по product.quantity. Передача
# данных в шаблон проходит аналогично варианту 1.
def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'lec6/total_count.html', context)

# В третьем случае возложим задачу по подсчёту общего количества продуктов на
# модель Product, а представление пробросит её в шаблон
# Представление ничего не вычисляет. Мы передаём модель Product в шаблон
# total_count.html. Внутри шаблона вызовем метод модели, подсчитывающий общее
# количество продуктов.
def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'lec6/total_count.html', context)