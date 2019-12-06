from rest_framework import serializers
from .models import StoreAssortment
from .models import Store


class StoreAssortmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreAssortment
        field = '_all_'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        field = '_all_'
