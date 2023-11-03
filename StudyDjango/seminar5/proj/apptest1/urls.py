from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='apptest1/index'),
               path('about/', views.about, name='apptest1/about'),
               path('coin/', views.coin, name='apptest1/coin'),
               path('cube/', views.cube, name='apptest1/cube'),
               path('myrand/', views.myrand, name='apptest1/myrand'),
               path('testlog/', views.testlog, name='apptest1/testlog'),
               ]
