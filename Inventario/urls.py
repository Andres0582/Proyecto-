from django.contrib import admin
from django.urls import path
from .views import (
    InventarioListCreateView, InventarioDetailView,
    StockListCreateView, StockDetailView,
    exportar_inventario_excel 
)

urlpatterns = [
    path('inventario/', InventarioListCreateView.as_view(), name='inventario-list-create'),
    path('inventario/<int:pk>/', InventarioDetailView.as_view(), name='inventario-detail'),

    path('stock/', StockListCreateView.as_view(), name='stock-list-create'),
    path('stock/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),

    # nueva URL para exportar
    path('exportar-inventario/', exportar_inventario_excel, name='exportar-inventario'),
]
