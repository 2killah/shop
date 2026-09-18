from rest_framework.generics import ListCreateAPIView
from .models import Game, Product
from .serializer import GameSerializer, ProductSerializer


class GameListCreateView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer