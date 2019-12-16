from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductDetailSerializer, ProductListSerializer, ShopDetailSerializer, ShopListSerializer
from .models import Product, Shop
from rest_framework.permissions import IsAuthenticated


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (IsAuthenticated,)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopDetailSerializer
    permission_classes = (IsAuthenticated,)


class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopDetailSerializer
    queryset = Shop.objects.all()
    permission_classes = (IsAuthenticated,)


class ShopListView(generics.ListAPIView):
    serializer_class = ShopListSerializer
    queryset = Shop.objects.all()
    permission_classes = (IsAuthenticated,)
