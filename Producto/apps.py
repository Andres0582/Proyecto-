from django.apps import AppConfig

# Configuración de la aplicación Producto
class ProductoConfig(AppConfig):
    # Define el tipo de campo automático por defecto para claves primarias
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nombre de la aplicación
    name = 'Producto'
