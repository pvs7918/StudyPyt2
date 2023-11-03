# Домашнее задание №4
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото
import datetime
from datetime import timezone

from django import forms


class CreateProductForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=200)
    price = forms.FloatField(min_value=0, required=True)
    quantity = forms.IntegerField(min_value=0, required=True)
    date_added = forms.DateField(initial=datetime.date.today,
                                 widget=forms.DateInput(attrs={
                                     'class': 'form-control',
                                     'type': 'date'}))
    foto = forms.ImageField()   # null=True, upload_to='media/' - попробовать добавить  blank=True, verbose_name='Фото'

    # в файле settings.py пропишем следующие пару констант:
    # MEDIA_URL = '/media/'
    # MEDIA_ROOT = BASE_DIR / 'media'
