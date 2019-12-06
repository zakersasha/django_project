from rest_framework import viewsets
from . import models
from . import serializers


class StoreAssortment(viewsets.ModelViewSet):
    queryset = models.StoreAssortment.objects.all()
    serializer_class = serializers.StoreAssortmentSerializer


class Store(viewsets.ModelViewSet):
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreSerializer
