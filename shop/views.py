from rest_framework import generics
from .serializers import ProductDetailSerializer, ProductListSerializer, ShopDetailSerializer, ShopListSerializer
from .models import Product, Shop


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopDetailSerializer


class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopDetailSerializer
    queryset = Shop.objects.all()


class ShopListView(generics.ListAPIView):
    serializer_class = ShopListSerializer
    queryset = Shop.objects.all()
