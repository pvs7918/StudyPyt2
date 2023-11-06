from django.contrib import admin

# Register your models here.

# Вернёмся к коду лекции 3. Если вы создавали для каждого занятия свой проект, в
# файле models.py из каталога myapp3 у вас будет хранится модель автора и статьи.
# Подключим их к админке через admin.py приложения myapp3.

from django.contrib import admin
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)

