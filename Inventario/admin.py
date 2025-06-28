from django.contrib import admin
from import_export.admin import ExportMixin                  # Mixin que permite exportar datos desde el admin
from import_export import resources                          # Clase base para definir recursos exportables
from .models import Inventario, Stock

# Esta clase le indica a django-import-export cómo manejar los datos del modelo Inventario
class InventarioResource(resources.ModelResource):
    class Meta:
        model = Inventario

# Hereda de ExportMixin para permitir la exportación de datos en formatos como CSV o Excel
class InventarioAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = InventarioResource
    list_display = ('fecha_inventario', 'producto', 'stock', 'comentario')  

# Definimos una clase recurso para el modelo Stock igual que en inventario
class StockResource(resources.ModelResource):
    class Meta:
        model = Stock   

# Creamos una clase personalizada del panel de administración para el modelo stock
class StockAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StockResource
    list_display = ('cantidad_stock', 'nombre_producto', 'categoria')  

# Finalmente registramos ambos modelos junto con sus clases de administrador personalizadas
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Stock, StockAdmin)
