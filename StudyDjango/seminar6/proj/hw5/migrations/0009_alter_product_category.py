# Generated by Django 4.2.6 on 2023-11-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw5', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(default=1),
        ),
    ]
