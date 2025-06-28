from rest_framework import serializers
from .models import Inventario, Stock


# Serializador para el modelo Inventario
# Convierte los datos del inventario (producto y fecha) en formato JSON y viceversa
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'fecha_inventario', 'producto', 'stock', 'comentario']



# Serializador para el modelo Stock
# Convierte los datos del stock (inventario y cantidad) en formato JSON y viceversa
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['cantidad_stock', 'nombre_producto', 'categoria']
        
