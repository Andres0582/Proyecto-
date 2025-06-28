from rest_framework import serializers
from .models import Asistencia

# Serializador para el modelo Usuario
class AsistenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'  # Todos los campos del modelo
