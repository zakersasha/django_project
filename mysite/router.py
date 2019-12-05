from shop.viewsets import Store_Assortment
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Store_Assortment', Store_Assortment)