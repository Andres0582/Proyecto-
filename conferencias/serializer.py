from rest_framework import serializers
from .models import Conferencias

class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencias
        fields = ['titulo', 'fecha', 'descripcion']  # deben coincidir con el modelo
