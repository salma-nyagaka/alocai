from django.urls import include, path

from .views import GamesApiView

urlpatterns = [
    path('games', GamesApiView.as_view(), name='create-game'),
]
