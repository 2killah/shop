from django.urls import path
from .views import GameListCreateView, ProductListCreateView

urlpatterns = [
    path('games/', GameListCreateView.as_view()),
    path('products/', ProductListCreateView.as_view()),
]