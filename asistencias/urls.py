from django.urls import path
from .views import asistencias_view

urlpatterns = [
    path('', asistencias_view, name='asistencias'),
]
