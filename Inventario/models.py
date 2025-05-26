from django.db import models

# Esta clase representa el inventario con la fecha que se realizo.
class Inventario(models.Model):
    # Aquí se guarda el día en que se realizó el inventario.
    fecha_inventario = models.DateField()

    # Al convertir un objeto de esta clase en texto, se intenta mostrar el nombre del producto relacionado.
    def __str__(self):
        return f'Inventario de {self.producto.nombre}'

# Esta clase sirve para registrar cuántas unidades de un producto hay en un inventario determinado.
class Stock(models.Model):
    # Aqui se establece una relación con la clase Inventario. Si se elimina el inventario, también se borra el stock asociado.
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    
    # Se usa para indicar cuántas unidades hay disponibles en ese inventario.
    cantidad_stock = models.IntegerField()

    # Al mostrar el stock como texto, se incluye la cantidad y el producto relacionado al inventario.
    def __str__(self):
         return f'Stock de {self.cantidad_stock} para {self.inventario.producto.nombre}'

