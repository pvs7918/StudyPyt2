# Generated by Django 4.2.6 on 2023-11-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sem5', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
