from django.contrib import admin 
from django.urls import path
from .views import (
    rol_lista_view, RolDetailView,
    PersonaListCreateView, PersonaDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # === ROL ===
    path('rol/', rol_lista_view.as_view(), name='rol-list-create'),
    path('rol/<int:pk>/', RolDetailView.as_view(), name='rol-detail'),

    # === PERSONA ===
    path('persona/', PersonaListCreateView.as_view(), name='persona-list-create'),
    path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
]
