from rest_framework import serializers
from .models import Rol, persona


# Serializador para el modelo Rol.
# Se encarga de convertir objetos Rol en formatos como JSON y viceversa.
class RolSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = Rol
        fields = ['nombre', 'descripcion']
=======
        model = Rol  # Se indica que este serializador trabajará con el modelo Rol.
        fields = ['nombre', 'descripcion']  # Se especifican los campos que serán expuestos o aceptados por la API.
>>>>>>> a6101a0e35955e351d35734992929a2a8cfe9736


# Serializador para el modelo Persona.
# Permite transformar datos del modelo Persona en JSON y también interpretar datos entrantes.
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = persona
        fields = ['nombre', 'correo', 'contraseña']
=======
        model = Persona  # Se asocia este serializador con el modelo Persona.
        fields = ['nombre', 'correo', 'contraseña', 'rol']  # Campos incluidos en las peticiones y respuestas.
>>>>>>> a6101a0e35955e351d35734992929a2a8cfe9736
