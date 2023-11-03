# Generated by Django 4.2.6 on 2023-11-03 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sem5', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=999999.99, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]