"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apptest1/', include('apptest1.urls')),
    path('myapp2/', include('myapp2.urls')),
    path('myapp3/', include('myapp3.urls')),
    path('lect4/', include('lect4.urls')),
    path('sem4/', include('sem4.urls')),
    path('lec6/', include('lec6.urls')),
    path('', include('hw5.urls')),     # Домашнее задание по семинару 5 в отдельном приложении
    # path('__debug__/', include("debug_toolbar.urls")),  # для работы инструмента Django Debug Toolbar
]

