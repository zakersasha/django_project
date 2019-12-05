from django.db import models


class Store_Assortment(models.Model):
    store_name = models.CharField(max_length=20)
    product = models.CharField(max_length=30)
    price = models.CharField(max_length=10)

