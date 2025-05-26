from django.contrib import admin 
from django.urls import path
from .views import (
    rol_lista_view, RolDetailView,
    PersonaListCreateView, PersonaDetailView
)

urlpatterns = [
    # Ruta para acceder al panel de administración de Django.
    path('admin/', admin.site.urls),

    # === ROL ===
    # Ruta que permite listar todos los roles o crear uno nuevo mediante una solicitud HTTP.
    path('rol/', rol_lista_view.as_view(), name='rol-list-create'),

    # Ruta que permite consultar, modificar o eliminar un rol específico a través de su ID.
    path('rol/<int:pk>/', RolDetailView.as_view(), name='rol-detail'),

    # === PERSONA ===
    # Ruta que permite listar todas las personas o registrar una nueva persona en el sistema.
    path('persona/', PersonaListCreateView.as_view(), name='persona-list-create'),

    # Ruta que permite acceder, actualizar o eliminar los datos de una persona específica, usando su ID.
    path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
]
