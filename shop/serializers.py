from rest_framework import  serializers
from .models import Store_Assortment

class Store_AssortmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store_Assortment
        field = '_all_'
