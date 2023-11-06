from django.urls import path

from . import views
from .views import product_add

urlpatterns = [path('', views.index, name='hw5/index'),  # myapp3/ добавлен потому что в приложении apptest1 такие же названия есть
               path('clients/', views.clients, name='hw5/clients'),
               path('client/<int:client_id>/', views.client, name='hw5/client'),
               path('products/', views.products, name='hw5/products'),
               path('product/<int:product_id>/', views.product, name='hw5/product'),
               path('product/add/', product_add, name='product_add'),   # http://127.0.0.1:8000/product/add/
               path('orders/', views.orders, name='hw5/orders'),
               path('orders_for_days/<int:days_cnt>/', views.orders_for_days, name='hw5/orders_for_days'),
               path('order_products/<int:order_id>/', views.order_products, name='hw5/order_products'),
               ]
