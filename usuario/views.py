from rest_framework import generics
from rest_framework.response import Response

from .models import Rol, persona
from .serializer import RolSerializer, PersonaSerializer


# === ROL ===
class rol_lista_view (generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
class RolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

# === PERSONA ===
class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer