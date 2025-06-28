from django.urls import path
from .views import ConferenciaListCreateView

urlpatterns = [
    path('conferencias/', ConferenciaListCreateView.as_view(), name='conferencia-list-create'),
]
