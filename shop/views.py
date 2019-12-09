from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product


class ArticleView(APIView):
    def get(self, request):
        articles = Product.objects.all()
        return Response({"articles": articles})
