from django.urls import path
from .views import (
    rol_lista_view, RolDetailView,
    PersonaListCreateView, PersonaDetailView,
    resumen_personas 
)

urlpatterns = [
    path('rol/', rol_lista_view.as_view(), name='rol-list-create'),
    path('rol/<int:pk>/', RolDetailView.as_view(), name='rol-detail'),

    path('persona/', PersonaListCreateView.as_view(), name='persona-list-create'),
    path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('persona/resumen/', resumen_personas, name='resumen-personas'),
]
