from rest_framework import serializers
from .models import Categoria, Producto, Venta 


# Serializador para el modelo Categoria
# Convierte los datos de la categoría (nombre y descripción) en formato JSON y viceversa
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']


# Serializador para el modelo Producto
# Convierte los datos del producto en formato JSON y viceversa
# Incluye nombre, descripción, stock, precio, fechas, categoría y persona asociada
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'precio', 'fecha_vencimiento', 'fecha_fabricacion']


# Serializador para el modelo Venta
# Convierte los datos de la venta en formato JSON y viceversa
# Incluye producto, cantidad vendida, fecha de la venta y total del precio
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['cantidad_producto', 'fecha_venta', 'total_precio', 'producto']
