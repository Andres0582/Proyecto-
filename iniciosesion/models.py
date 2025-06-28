from django.db import models

# Modelo para representar un usuario del sistema
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)  # En la práctica, se debe encriptar

    def __str__(self):
        return self.nombre_usuario
