# Generated by Django 4.2.6 on 2023-10-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0002_rename_summ_order_order_summ'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='foto',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
