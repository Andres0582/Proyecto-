from django.shortcuts import render  # se utiliza para darle un renderizado a la  pagina
from .models import Venta
import plotly.graph_objs as go       # Es la libreria para crear el grafico
import plotly.offline as opy         # para poder ver el grafico en un archivo html

def grafico_ventas(request):
    # consulta en la tabla ventas la informacion de producto
    ventas = Venta.objects.select_related('producto')

    # se crea un diccionario el cual va a almacenar la informacion de la base de datos
    datos = {}

    # busca en toda la tabla de ventas
    for venta in ventas:
        # se saca el nombre del producto
        nombre = venta.producto.nombre

        # se suma el total de cada producto vendido 
        datos[nombre] = datos.get(nombre, 0) + float(venta.total_precio)

    productos = list(datos.keys())    # crea una lista con el nombre de los productos encontrados
    totales = list(datos.values())    # una lista con los totales vendidos por cada producto

    # creamos el grafico con la libreria
    trace = go.Bar(
        x=productos,                 # se le da un nombre al eje x
        y=totales,                   # se le da un nombre al eje y
        marker_color='orange'        # se le da un color a las barras del grafico
    )

    # se configura el grafico
    layout = go.Layout(
        title='Ventas Totales por Producto',  # se le asigna un nombre del grafico 
        xaxis_title='Producto',               # nombre de la linea de eje x
        yaxis_title='Total Vendido ($)'       # nombre de la linea de eje y
    )

    # se crea la figura combinando los datos obtenidos
    fig = go.Figure(data=[trace], layout=layout)

    # pasamos el grafico a un html
    grafico_html = opy.plot(fig, auto_open=False, output_type='div')

    return render(request, 'grafico_ventas.html', {'grafico': grafico_html})
