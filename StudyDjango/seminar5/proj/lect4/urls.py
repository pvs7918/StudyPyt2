from django.urls import path
from .views import user_form, many_fields_form, add_user, upload_image

# А теперь прописываем маршрут для связи представления с url-адресом. Для этого
# создаём urls.py внутри каталога приложения:

urlpatterns = [
    # Форма будет доступна по адресу
    path('user/add/', user_form, name='user_form'),   # http://127.0.0.1:8000/lect4/user/add/
    path('user/', add_user, name='add_user'),   # http://127.0.0.1:8000/lect4/user/
    path('forms/', many_fields_form, name='many_fields_form'),
    path('upload/', upload_image, name='upload_image'),  # http://127.0.0.1:8000/lect4/upload/
]