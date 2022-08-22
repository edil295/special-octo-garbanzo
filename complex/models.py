from django.db import models


class Block(models.Model):
    number_block = models.CharField(max_length=100, verbose_name='Номер блока')
    price_square_meter = models.IntegerField(verbose_name='Стоимость за квадратный метр квартиры')
    count_entrance = models.IntegerField(verbose_name='Количество подъездов')
    count_floors = models.IntegerField(verbose_name='Количество этажей')
    apartment_count = models.IntegerField(verbose_name='Количество квартир на этаже')

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return self.number_block


class Client(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='ФИО владельца квартиры')
    date_of_sale = models.DateField(blank=True, null=True, verbose_name='Дата продажи')
    status = models.CharField(max_length=100, choices=[('Выкуп', 'Выкуп'),
                                                       ('Выкуп не до конца', 'Выкуп не до конца'),
                                                       ('Расторгнуто', 'Расторгнуто'),
                                                       ('Не продано', 'Не продано')],
                              verbose_name='Статус')
    area = models.IntegerField(verbose_name='Общая площадь')
    client_block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Блок')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return ''
