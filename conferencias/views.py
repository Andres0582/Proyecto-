from rest_framework import generics
from .models import Conferencias
from .serializer import ConferenciaSerializer

class ConferenciaListCreateView(generics.ListCreateAPIView):
    queryset = Conferencias.objects.all()
    serializer_class = ConferenciaSerializer
