from rest_framework import generics
from django.db import models
from .models import Categoria, Producto, Venta
from .serializer import CategoriaSerializer, ProductoSerializer, VentaSerializer
import plotly.graph_objects as go # generar el grafico 
from django.http import HttpResponse 
from django.template import loader # para cargar una plantilla html


class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# === VENTA ===

class VentaListCreateView(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VentaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

# se define una vista llamada 
def grafico_ventas_por_producto(request):
    
    # Venta.objects.values accede a los valores del modelo venta especificamente el nombre del producto relacionado
    # producto__nombre accede a un campo del modelo relacionado
    # annotate agrega un campo adicional a los resultados agrupados, en este caso el total de ventas por producto
    # models.Count('id') es una funcion de agregacion que cuenta cuantas veces aparece cada producto
    # order_by('-total') ordena los resultados de forma descendente por la cantidad total de ventas
    datos = Venta.objects.values('producto__nombre').annotate(
        total=models.Count('id')
    ).order_by('-total')

    # Se crea una lista por comprensión para extraer solo los nombres de los productos
    productos = [item['producto__nombre'] for item in datos]

    # Se crea otra lista por comprension para extraer los totales de ventas correspondientes a cada producto
    totales = [item['total'] for item in datos]

    # Se crea un gráfico de barras con Plotly
    # go.Figure construye un grafico 
    # go.Bar representa un grafico de barras con valores en X (productos) y Y (ventas)
    fig = go.Figure(data=[go.Bar(x=productos, y=totales)])

    # Se configura el diseño del gráfico
    # `update_layout(...)` permite modificar el diseño, títulos y ejes del gráfico creado
    # Cada parámetro define el texto que se verá en el gráfico
    fig.update_layout(
        title='Ventas por Producto',        # Título principal del gráfico
        xaxis_title='Producto',             # Título del eje horizontal (eje X)
        yaxis_title='Cantidad de Ventas'    # Título del eje vertical (eje Y)
    )

    # `fig.to_html(...)` convierte el gráfico en código HTML para incrustarlo en una página web
    # `full_html=False` significa que solo se genera el <div> del gráfico, no un documento HTML completo
    grafico_html = fig.to_html(full_html=False)

    # Se carga una plantilla HTML usando `loader.get_template(...)`
    # `loader` es una utilidad de Django que permite cargar archivos de plantilla ubicados en la carpeta templates
    template = loader.get_template('grafico.html')

    # Se define un diccionario llamado `contexto` que contiene el gráfico generado en HTML
    # Este diccionario será enviado a la plantilla para ser renderizado
    contexto = {'grafico': grafico_html}

    # Se devuelve una respuesta HTTP con la plantilla renderizada
    # `HttpResponse(...)` genera una respuesta web estándar
    # `template.render(contexto, request)` dibuja la plantilla con los datos del contexto y la solicitud del usuario
    return HttpResponse(template.render(contexto, request))
