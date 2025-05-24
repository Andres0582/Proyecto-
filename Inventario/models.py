from django.db import models

class Inventario(models.Model):
    fecha_inventario = models.DateField()

    def __str__(self):
        return f'Inventario de {self.producto.nombre}'


class Stock(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad_stock = models.IntegerField()

    def __str__(self):
         return f'Stock de {self.cantidad_stock} para {self.inventario.producto.nombre}'
     
     