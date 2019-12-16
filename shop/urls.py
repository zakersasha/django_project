from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('product/create/', ProductCreateView.as_view()),
    path('products/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
    path('shop/create/', ShopCreateView.as_view()),
    path('', ShopListView.as_view()),
    path('shop/detail/<int:pk>/', ShopDetailView.as_view()),
]