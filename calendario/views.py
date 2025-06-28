from rest_framework import generics
from .models import Evento
from .serializars import EventoSerializer

class EventoListCreateView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
