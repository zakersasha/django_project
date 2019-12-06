from django.db import models


class StoreAssortment(models.Model):
    store_id = models.UUIDField(primary_key=True)
    product = models.CharField(max_length=30)
    price = models.IntegerField()


class Store(models.Model):
    store_id = models.UUIDField(primary_key=True)
    store_name = models.CharField(max_length=20)
    street_name = models.CharField(max_length=40)