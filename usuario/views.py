from rest_framework import generics
from rest_framework.response import Response
from .models import Rol, persona
from .serializer import RolSerializer, PersonaSerializer
import pandas as pd
from django.http import JsonResponse


class rol_lista_view(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = persona.objects.all()
    serializer_class = PersonaSerializer


# Esta función genera un resumen estadístico sobre las personas registradas en la base de datos.
def resumen_personas(request):

    # Se obtiene un queryset de todas las personas, seleccionando solo algunos campos:
    # id, nombre, apellido, correo, teléfono y el nombre del rol relacionado.
    personas_qs = persona.objects.all().values(
        'id', 'nombre', 'apellido', 'correo', 'telefono', 'rol__nombre'
    )

    # Se convierte el queryset en un DataFrame de pandas para facilitar el análisis.
    df = pd.DataFrame(list(personas_qs))

    # Se renombra la columna 'rol__nombre' a simplemente 'rol' para mayor claridad.
    df.rename(columns={'rol__nombre': 'rol'}, inplace=True)

    # Cálculo del total de personas en el sistema.
    total_personas = len(df)

    # Cálculo de cuántas personas hay por cada tipo de rol.
    # Se hace un conteo de los valores únicos de la columna 'rol'.
    personas_por_rol = df['rol'].value_counts().to_dict()

    # Se calcula la longitud promedio de los nombres, excluyendo valores nulos.
    longitud_promedio_nombre = round(df['nombre'].dropna().apply(len).mean(), 2)

    # Se calcula cuántas personas no tienen número de teléfono.
    # Se suman los valores nulos y los que están vacíos ('').
    personas_sin_telefono = int(df['telefono'].isnull().sum() + (df['telefono'] == '').sum())

    # Se obtiene el dominio de los correos (parte después del '@') y se cuentan cuántos hay de cada uno.
    dominios_correo = df['correo'].dropna().apply(lambda x: x.split('@')[-1]).value_counts().to_dict()

    # Se construye el resumen con todas las estadísticas calculadas.
    resumen = {
        'total_personas': total_personas,
        'personas_por_rol': personas_por_rol,
        'longitud_promedio_nombre': longitud_promedio_nombre,
        'personas_sin_telefono': personas_sin_telefono,
        'correos_por_dominio': dominios_correo
    }

    # Se devuelve el resumen en formato JSON como respuesta al cliente.
    return JsonResponse(resumen)
