from django.db import models


class StoreAssortment(models.Model):
    store_name = models.CharField(max_length=20)
    product = models.CharField(max_length=30)
    price = models.IntegerField(max_length=10)


class Store(models.Model):
    store_name = models.CharField(max_length=20)
    street_name = models.CharField(max_length=40)