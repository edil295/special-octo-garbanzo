# Generated by Django 3.2 on 2022-08-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complex', '0006_alter_client_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='price_square_meter',
            field=models.IntegerField(verbose_name='Стоимость за квадратный метр квартиры'),
        ),
    ]
