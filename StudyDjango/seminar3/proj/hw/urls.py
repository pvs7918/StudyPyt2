from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='hw/index'),  # myapp3/ добавлен потому что в приложении apptest1 такие же названия есть
               path('clients/', views.clients, name='hw/clients'),
               path('client/<int:client_id>/', views.client, name='hw/client'),
               path('products/', views.products, name='hw/products'),
               path('product/<int:product_id>/', views.product, name='hw/product'),
               path('orders/', views.orders, name='hw/orders'),
               path('orders_for_days/<int:days_cnt>/', views.orders_for_days, name='hw/orders_for_days'),
               path('order_products/<int:order_id>/', views.order_products, name='hw/order_products'),


               # path('client_orders/<int:client_id>/', views.client_orders, name='hw/client_orders'),
               # path('client_products/<int:order_id>/<int:days>/', views.client_products, name='hw/client_products'),
               # path('order/<int:order_id>/', views.order, name='hw/order'),
               ]
