
from rest_framework import generics
from .models import Categoria, Producto, Venta
from .serializer import CategoriaSerializer, ProductoSerializer, VentaSerializer

# === CATEGORIA ===

# Esta clase permite consultar todas las categorías registradas o añadir una nueva.
# Funciona con métodos GET y POST.
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()  # Se obtienen todos los registros del modelo Categoria.
    serializer_class = CategoriaSerializer  # Se indica el serializador que transforma los datos para la API.

# Esta clase maneja operaciones sobre una categoría específica:
# permite verla, modificarla o eliminarla (GET, PUT/PATCH, DELETE).
class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# === PRODUCTO ===

# Clase que permite obtener todos los productos existentes o crear un nuevo producto.
# Responde a métodos GET y POST.
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()  # Se consultan todos los productos registrados.
    serializer_class = ProductoSerializer  # Se utiliza este serializador para traducir los datos.

# Clase que permite consultar, actualizar o borrar un producto en particular según su ID.
class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# === VENTA ===

# Esta vista permite consultar el historial de ventas o registrar una nueva venta.
# Trabaja con GET (listar) y POST (crear).
class VentaListCreateView(generics.ListCreateAPIView):
    queryset = Venta.objects.all()  # Se accede a todos los registros del modelo Venta.
    serializer_class = VentaSerializer  # Convierte entre objetos de modelo y datos JSON.

# Vista diseñada para trabajar con una venta concreta: obtener su información, modificarla o eliminarla.
class VentaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
