# Generated by Django 4.2.6 on 2023-11-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw5', '0004_alter_product_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
    ]
