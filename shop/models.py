from django.db import models


class Shop(models.Model):
    name = models.CharField(verbose_name='Название магазина', max_length=30)
    address = models.CharField(verbose_name='Адрес магазина', max_length=30)


class Product(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='Магазин', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование', max_length=30)
    producer = models.CharField(verbose_name='Прозводитель', max_length=30)
    release_date = models.DateField(verbose_name='Дата изготовления')
    price = models.DecimalField(verbose_name='Цена', help_text='*в рублях', max_digits=7, decimal_places=2)
