from shop.viewsets import StoreAssortment
from shop.viewsets import Store
from rest_framework import routers

router = routers.DefaultRouter()
router.register('StoreAssortment', StoreAssortment)
router = routers.DefaultRouter()
router.register('Store', Store)