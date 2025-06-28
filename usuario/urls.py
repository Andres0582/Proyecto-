from django.urls import path
from .views import (
    rol_lista_view, RolDetailView,
    PersonaListCreateView, PersonaDetailView,
    resumen_personas 
)

urlpatterns = [
<<<<<<< HEAD
=======
    # Ruta para acceder al panel de administración de Django.
    path('admin/', admin.site.urls),

    # === ROL ===
    # Ruta que permite listar todos los roles o crear uno nuevo mediante una solicitud HTTP.
>>>>>>> a6101a0e35955e351d35734992929a2a8cfe9736
    path('rol/', rol_lista_view.as_view(), name='rol-list-create'),

    # Ruta que permite consultar, modificar o eliminar un rol específico a través de su ID.
    path('rol/<int:pk>/', RolDetailView.as_view(), name='rol-detail'),

<<<<<<< HEAD
=======
    # === PERSONA ===
    # Ruta que permite listar todas las personas o registrar una nueva persona en el sistema.
>>>>>>> a6101a0e35955e351d35734992929a2a8cfe9736
    path('persona/', PersonaListCreateView.as_view(), name='persona-list-create'),

    # Ruta que permite acceder, actualizar o eliminar los datos de una persona específica, usando su ID.
    path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('persona/resumen/', resumen_personas, name='resumen-personas'),
]
