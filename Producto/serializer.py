from rest_framework import serializers
from .models import Categoria, Producto, Venta 


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'precio', 'fecha_vencimiento', 'fecha_fabricabion', 'categoria', 'persona']
        
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['prodcuto', 'cantidad_producto', 'fecha_venta', 'total_precio']
        
        