from django.db import models

# Modelo para representar un usuario del sistema
class Evento(models.Model):
    nombre_evento = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField()
    hora_inicio = models.TimeField()  # En la práctica, se debe encriptar
    hora_fin = models.TimeField()


    def __str__(self):
        return self.nombre_evento
