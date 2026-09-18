import pytest
from rest_framework.test import APIClient

from .models import Game
from .serializer import GameSerializer

@pytest.mark.django_db
def test_game_creation():
    game = Game.objects.create(
        name="Minecraft", 
        genre="Sandbox", 
        price=10000
    )

    assert game.name == "Minecraft"


@pytest.mark.django_db
def test_game_serializer():
    game = Game.objects.create(
        name="Minecraft",
        genre="Sandbox",
        price=10000
    )

    serializer = GameSerializer(game)

    assert serializer.data['name'] == "Minecraft"


@pytest.mark.django_db
def test_get_games():
    Game.objects.create(
        name="Minecraft",
        genre="Sandbox",
        price=10000
    )

    client = APIClient()
    response = client.get('/api/games/')

    assert response.status_code == 200
    assert len(response.data) == 1