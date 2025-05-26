from django.contrib import admin
from django.urls import path
from .views import (
    CategoriaListCreateView, CategoriaDetailView,
    ProductoListCreateView, ProductoDetailView,
    VentaListCreateView, VentaDetailView
)

# Lista de rutas que define cómo se accede a cada recurso de la API desde la web.
urlpatterns = [
    # Dirección para ingresar al panel administrativo que ofrece Django por defecto.
    path('admin/', admin.site.urls),

    # === CATEGORIA ===
    # Ruta que permite mostrar todas las categorías existentes o registrar una nueva.
    path('categoria/', CategoriaListCreateView.as_view(), name='categoria-list-create'),

    # Ruta para ver, editar o eliminar una categoría específica según su ID.
    path('categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),

    # === PRODUCTO ===
    # Ruta para acceder a la lista de productos o crear uno nuevo en el sistema.
    path('producto/', ProductoListCreateView.as_view(), name='producto-list-create'),

    # Ruta para obtener los detalles de un producto, actualizarlo o eliminarlo según su ID.
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),

    # === VENTA ===
    # Ruta que permite ver todas las ventas registradas o añadir una nueva.
    path('venta/', VentaListCreateView.as_view(), name='venta-list-create'),

    # Ruta para consultar, modificar o borrar una venta específica, identificada por su ID.
    path('venta/<int:pk>/', VentaDetailView.as_view(), name='venta-detail'),
]
