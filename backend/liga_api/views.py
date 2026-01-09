from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Liga, 
    Equipa,
    Jogador, 
    Jogo
)
from .serializer import (
    LigaSerializer,
    EquipaSerializer,
    JogadorSerializer,
    JogoSerializer
)

# Create your views here.
class LigaViewSet(viewsets.ModelViewSet):
    queryset = Liga.objects.all()
    serializer_class = LigaSerializer
    permission_classes = [permissions.AllowAny]

class EquipaViewSet(viewsets.ModelViewSet):
    queryset = Equipa.objects.all()
    serializer_class = EquipaSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET']) # permite filtrar uma determinada liga de acordo com o id
def equipas_por_liga(request, liga_id):
    equipas = Equipa.objects.filter(liga_id=liga_id)
    serializer = EquipaSerializer(equipas, many=True)
    return Response(serializer.data)
    
class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    permission_classes = [permissions.AllowAny]

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    permission_classes = [permissions.AllowAny]

