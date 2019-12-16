from rest_framework import serializers
from .models import Product, Shop


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'shop', 'name', 'price')


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'address')
