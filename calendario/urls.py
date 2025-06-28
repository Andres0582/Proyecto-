from django.urls import path
from .views import EventoListCreateView

urlpatterns = [
    path('eventos/', EventoListCreateView.as_view(), name='evento-list-create'),
]
