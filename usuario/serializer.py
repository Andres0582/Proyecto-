from rest_framework import serializers
from .models import Rol, Persona


# Serializador para el modelo Rol.
# Se encarga de convertir objetos Rol en formatos como JSON y viceversa.
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol  # Se indica que este serializador trabajará con el modelo Rol.
        fields = ['nombre', 'descripcion']  # Se especifican los campos que serán expuestos o aceptados por la API.


# Serializador para el modelo Persona.
# Permite transformar datos del modelo Persona en JSON y también interpretar datos entrantes.
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona  # Se asocia este serializador con el modelo Persona.
        fields = ['nombre', 'correo', 'contraseña', 'rol']  # Campos incluidos en las peticiones y respuestas.
