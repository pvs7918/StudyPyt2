from django.shortcuts import render

import logging
from .forms import UserForm, ManyFieldsForm, ImageForm
from .models import User
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


# Следующий этап — использовать представление для перевода формы из класса в
# видимый пользователем HTML, а также для обработки данных, которые
# пользователь введёт в форму и отправит на сервер.
# Для вывода формы по GET запросу и обработки данных по POST запросу в Django
# можно использовать следующий код:

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)  # создаем форму с переданными данными
        if form.is_valid():
            # Если форма проходит валидацию(все поля заполнены корректно), то мы получаем данные
            # из формы и можем с ними работать.
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            # Метод user.save() сохраняет запись в таблицу БД.
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        # Если запрос пришел методом GET, то мы просто создаем пустой экземпляр формы UserForm
        # и передаем его в шаблон user_form.html.
        form = UserForm()
        # В шаблоне user_form.html мы можем вывести нашу форму с помощью тега {{form}}.
        message = 'Заполните форму'
        return render(request, 'lect4/user_form.html',
                      {'form': form, 'message': message})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
        return render(request, 'lect4/user_form.html',
                      {'form': form, 'message': message})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
        return render(request, 'lect4/many_fields_form.html',
                      {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
        # Если поступил POST запрос, форма заполняется не только из request.POST, но и из
        # request.FILES. Там содержится наше изображение. Если проверка формы успешно
        # завершены, выполняем три действия:
        # 1. Сохраняем изображение в переменной image
        # 2. Создаём экземпляр класса FileSystemStorage для работы с файлами силами
        # Django
        # 3. Просим экземпляр fs сохранить изображение. Метод save принимает имя
        # файла и сам файл

    else:
        form = ImageForm()
        return render(request, 'lect4/upload_image.html', {'form': form})
