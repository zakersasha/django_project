from rest_framework import viewsets
from . import models
from . import serializers

class Store_Assortment(viewsets.ModelViewSet):
    queryset = models.Store_Assortment.objects.all()
    serializer_class = serializers.Store_AssortmentSerializer