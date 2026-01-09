from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LigaViewSet,
    EquipaViewSet,
    JogadorViewSet,
    JogoViewSet,
    equipas_por_liga
)

router = DefaultRouter()
router.register(r'ligas', LigaViewSet)
router.register(r'equipas', EquipaViewSet)
router.register(r'jogadores', JogadorViewSet)
router.register(r'jogos', JogoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ligas/<int:liga_id>/equipas/', equipas_por_liga)
]