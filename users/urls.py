from django.conf.urls import url
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    url(r'create/', CreateUserAPIView.as_view()),
    url(r'update/', UserRetrieveUpdateAPIView.as_view()),
]