from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('/login/', TokenObtainPairView.as_view()),
    path('/token/refresh/', TokenRefreshView.as_view()),
    *router.urls
]