from django.contrib import admin
from django.urls import path
from .views import (
    InventarioListCreateView, InventarioDetailView,
    StockListCreateView, StockDetailView
)

# Aquí se define la lista de rutas (URL patterns) que manejará la aplicación.
urlpatterns = [
    # Ruta para acceder al panel de administración de Django.
    path('admin/', admin.site.urls),

    # === INVENTARIO ===
    # Ruta que permite ver todos los registros de inventario existentes o si necesita crear uno nuevo.
    path('inventario/', InventarioListCreateView.as_view(), name='inventario-list-create'),

    # Ruta para consultar, modificar o eliminar un inventario específico, identificado por su ID.
    path('inventario/<int:pk>/', InventarioDetailView.as_view(), name='inventario-detail'),

    # === STOCK ===
    # Ruta para ver todos los registros de stock o agregar uno nuevo.
    path('stock/', StockListCreateView.as_view(), name='stock-list-create'),

    # Ruta para trabajar con un registro de stock en particular, usando su ID como identificador.
    path('stock/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
]
