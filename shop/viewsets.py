from rest_framework import viewsets
from . import models
from . import serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects
    serializer_class = serializers.ProductSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = models.Store.objects
    serializer_class = serializers.StoreSerializer
