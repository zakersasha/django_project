from rest_framework import serializers
from .models import Product
from .models import Store


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        field = '__all__'
