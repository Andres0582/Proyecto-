from rest_framework import serializers
from .models import Inventario, Stock


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['producto', 'fecha_inventario']
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['inventario', 'cantidad_stock']
        
