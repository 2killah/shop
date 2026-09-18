from rest_framework.generics import ListCreateAPIView
from .models import Game
from .serializer import GameSerializer

class GameListCreateView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer