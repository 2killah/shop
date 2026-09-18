import pytest
from rest_framework.test import APIClient

from .models import Game, Product
from .serializer import GameSerializer, ProductSerializer

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
    assert response.data[0]['name'] == "Minecraft"

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name="Phone", 
        price=50000
    )

    assert product.name == "Phone"

@pytest.mark.django_db
def test_product_serializer():
    product = Product.objects.create(
        name="Phone",
        price=50000
    )

    serializer = ProductSerializer(product)

    assert serializer.data['name'] == "Phone"

@pytest.mark.django_db
def test_product_serializer_description():
    product = Product.objects.create(
        name="Phone",
        price=50000,
        description="Smartphone"
    )

    serializer = ProductSerializer(product)

    assert serializer.data['description'] == "Smartphone"

@pytest.mark.django_db
def test_get_products():
    Product.objects.create(
        name="Phone",
        price=50000,
        description="Smartphone"
    )

    client = APIClient()
    response = client.get('/api/products/')

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == "Phone"