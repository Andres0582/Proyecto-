from django.db import models

# Modelo para guardar una foto de asistencia
class Asistencia(models.Model):
    fotopath = models.ImageField(upload_to='asistencias/')  # Carpeta en MEDIA_ROOT

    def __str__(self):
        return str(self.fotopath)
