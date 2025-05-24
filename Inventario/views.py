from rest_framework import generics
from .models import Inventario, Stock
from .serializer import InventarioSerializer, StockSerializer

# === INVENTARIO ===

class InventarioListCreateView(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class InventarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


# === STOCK ===

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
