# Generated by Django 4.2.6 on 2023-10-19 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_client_product_alter_coin_coin_variant_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coin',
            new_name='SaveCoin',
        ),
    ]
