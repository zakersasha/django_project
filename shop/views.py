from rest_framework import viewsets, permissions
from .serializers import ProductDetailSerializer, ShopDetailSerializer
from .models import Product, Shop


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly


