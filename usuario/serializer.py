from rest_framework import serializers
from .models import Rol, Persona


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['nombre', 'descepcion']


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre', 'correo', 'contraseña', 'rol']