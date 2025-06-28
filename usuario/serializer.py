from rest_framework import serializers
from .models import Rol, persona


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['nombre', 'descripcion']


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = ['nombre', 'correo', 'contraseña']