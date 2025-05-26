from rest_framework import generics
from .models import Inventario, Stock
from .serializer import InventarioSerializer, StockSerializer

# === INVENTARIO ===

# Esta vista permite consultar la lista completa de los inventarios existentes
# o agregar un nuevo registro. Se usa para operaciones de tipo GET y POST.
class InventarioListCreateView(generics.ListCreateAPIView):

    # Define la fuente de datos, en este caso todos los objetos del modelo Inventario.
    queryset = Inventario.objects.all()

    # Especifica qué clase se encargará de convertir los datos del modelo a JSON y viceversa.
    serializer_class = InventarioSerializer

# Esta vista se utiliza para obtener los detalles de un inventario específico,
# así como para editarlo o eliminarlo usando métodos GET, PUT, PATCH o DELETE.
class InventarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


# === STOCK ===

# Vista que permite ver todos los registros de stock o crear un nuevo registro.
# Se usa principalmente con métodos GET y POST.
class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

# Vista orientada a manejar operaciones sobre un solo registro de stock,
# ya sea para consultarlo, actualizarlo o eliminarlo.
class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
