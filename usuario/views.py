from rest_framework import generics
from rest_framework.response import Response

from .models import Rol, persona
from .serializer import RolSerializer, PersonaSerializer


# === ROL ===

# Vista que permite obtener la lista completa de roles o crear uno nuevo.
# Soporta métodos GET para listar y POST para crear.
class rol_lista_view(generics.ListCreateAPIView):
    queryset = Rol.objects.all()  # Se consulta toda la tabla de roles.
    serializer_class = RolSerializer  # Se usa este serializador para transformar los datos.


# Vista que gestiona operaciones sobre un rol específico identificado por su ID:
# permite obtener, actualizar o eliminar ese registro.
class RolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


# === PERSONA ===

# Vista que facilita listar todas las personas registradas o añadir una persona nueva.
# Atiende solicitudes GET (listar) y POST (crear).
class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = persona.objects.all()  # Se accede a todos los registros del modelo persona.
    serializer_class = PersonaSerializer  # Se aplica el serializador correspondiente.


# Vista que maneja una persona en particular, permitiendo:
# obtener su información, actualizarla o eliminarla, usando su clave primaria.
class PersonaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer
