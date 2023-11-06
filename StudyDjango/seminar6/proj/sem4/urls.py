from django.urls import path
from .views import form_game

urlpatterns = [
    # Форма будет доступна по адресу
    path('game/', form_game, name='form_game'),   # http://127.0.0.1:8000/sem4/game/
    # path('add_author/', add_author, name='add_author'),   # http://127.0.0.1:8000/sem4/add_author/

]
