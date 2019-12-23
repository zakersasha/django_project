from django.db import models
from user.models import User

User = User()


class Shop(models.Model):
    shop_types = (
        (1, 'Семья'),
        (2, 'Пятерочка'),
        (3, 'Магнит'),
    )
    name = models.CharField(verbose_name='Название магазина', choices=shop_types, max_length=30)
    address = models.CharField(verbose_name='Адрес магазина', max_length=30)


class Product(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='Магазин', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование', max_length=30)
    producer_types = (
        (1, 'Кунгурский производитель'),
        (2, 'Пермский производитель'),
        (3, 'Московский производитель'),
    )
    producer_type = models.IntegerField(verbose_name='Прозводитель', choices=producer_types)
    release_date = models.DateField(verbose_name='Дата изготовления')
    price = models.DecimalField(verbose_name='Цена', help_text='*в рублях', max_digits=7, decimal_places=2)
