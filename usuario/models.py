from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class persona(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=60)
    contraseña = models.CharField(max_length=20)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

