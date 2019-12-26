from django.urls import path, include
from shop import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Products', views.ProductView)
router.register('Shops', views.ShopView)

urlpatterns = [
    path('', include(router.urls)),
]
