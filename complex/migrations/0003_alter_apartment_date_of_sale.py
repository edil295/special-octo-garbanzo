# Generated by Django 3.2 on 2022-08-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complex', '0002_auto_20220821_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='date_of_sale',
            field=models.DateField(blank=True, null=True, verbose_name='Дата продажи'),
        ),
    ]