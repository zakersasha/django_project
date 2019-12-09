from shop.viewsets import ProductViewSet
from shop.viewsets import StoreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('StoreAssortment', ProductViewSet)
router = routers.DefaultRouter()
router.register('Store', StoreViewSet)