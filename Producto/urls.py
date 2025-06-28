from django.contrib import admin
from django.urls import path
from .views import (
    CategoriaListCreateView, CategoriaDetailView,
    ProductoListCreateView, ProductoDetailView,
    VentaListCreateView, VentaDetailView,
    grafico_ventas_por_producto
)

urlpatterns = [
    path('categoria/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),

    path('producto/', ProductoListCreateView.as_view(), name='producto-list-create'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),

    path('venta/', VentaListCreateView.as_view(), name='venta-list-create'),
    path('venta/<int:pk>/', VentaDetailView.as_view(), name='venta-detail'),

    path('grafico-ventas/', grafico_ventas_por_producto, name='grafico-ventas'),
]
