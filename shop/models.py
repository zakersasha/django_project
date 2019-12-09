from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(help_text='in rubles')

    def __str__(self) -> str:
        return self.name
