from django.db import models

# Esta clase representa el inventario con la fecha que se realizo.
class Inventario(models.Model):
    # Aquí se guarda el día en que se realizó el inventario.
    fecha_inventario = models.DateField()
    producto = models.CharField(max_length=80, default='Sin categoría')
    stock = models.CharField(max_length=80, default='Sin categoría')
    comentario = models.CharField(max_length=80, default='Sin categoría')
    # Al convertir un objeto de esta clase en texto, se intenta mostrar el nombre del producto relacionado.
    def __str__(self):
        return f'Inventario de {self.nombre}'

# Esta clase sirve para registrar cuántas unidades de un producto hay en un inventario determinado.
class Stock(models.Model):
    
    # Se usa para indicar cuántas unidades hay disponibles en ese inventario.
    cantidad_stock = models.IntegerField()
    nombre_producto = models.CharField(max_length=100, default='Sin categoría')
    categoria = models.CharField(max_length=50, default='Sin categoría')
    # Al mostrar el stock como texto, se incluye la cantidad y el producto relacionado al inventario.
    def __str__(self):
         return f'Stock de {self.cantidad_stock} para {self.nombre}'

