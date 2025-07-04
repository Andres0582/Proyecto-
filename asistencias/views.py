from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Asistencia
from .serializers import AsistenciasSerializer

# Vista para listar y crear usuarios
@api_view(['GET', 'POST'])
def asistencias_view(request):
    if request.method == 'GET':
        asistencias = Asistencia.objects.all()
        serializer = AsistenciasSerializer(asistencias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AsistenciasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
