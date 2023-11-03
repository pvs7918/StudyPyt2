from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='myapp3/index'),  # myapp3/ добавлен потому что в приложении apptest1 такие же названия есть
               path('about/', views.about, name='myapp3/about'),
               path('coin/<int:count>/', views.coin, name='coin'),
               path('cube/<int:count>/', views.cube, name='cube'),
               path('number_random/<int:count>/', views.number_random, name='number_random'),
               path('author_posts/<int:author_id>/', views.author_posts, name='myapp3/author_posts'),
               path('post/<int:post_id>/', views.post_view, name='myapp3/post_view'),
               ]
