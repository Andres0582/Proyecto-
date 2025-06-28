from rest_framework import generics
from .models import Inventario, Stock
from .serializer import InventarioSerializer, StockSerializer
from django.http import HttpResponse
from import_export.resources import ModelResource
from import_export.formats.base_formats import XLSX


class InventarioListCreateView(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class InventarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class InventarioResource(ModelResource):
    class Meta:
        model = Inventario


def exportar_inventario_excel(request):
    # usamos la clase InventarioResource para acceder a los datos del modelo de inventario
    dataset = InventarioResource().export()

    # XLSX() es el formato de exportación proporcionado por django-import-export
    export_data = XLSX().export_data(dataset)

    # establecemos el tipo de contenido correspondiente a archivos .xlsx
    response = HttpResponse(
        export_data, 
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    # indicamos que el archivo debe descargarse con el nombre "inventario.xlsx"
    response['Content-Disposition'] = 'attachment; filename="inventario.xlsx"'

    # retornamos la respuesta para que el navegador descargue el archivo
    return response
