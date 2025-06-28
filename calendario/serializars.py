
from rest_framework import serializers
from .models import Evento

# Serializador para el modelo Usuario
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'descripcion', 'hora_inicio', 'hora_fin']
