from django.db import models

# Modelo para la categoría de los productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)           # Nombre de la categoría
    descripcion = models.CharField(max_length=50)      # Descripción de la categoría

    def __str__(self):
        return self.nombre                             # Representación legible del objeto


# Modelo para representar un producto
class Producto(models.Model):
    nombre = models.CharField(max_length=50)           # Nombre del producto
    descripcion = models.CharField(max_length=60)      # Descripción del producto
    stock = models.IntegerField()                      # Cantidad disponible en inventario
    precio = models.FloatField()                       # Precio por unidad
    fecha_vencimiento = models.DateTimeField()         # Fecha de vencimiento del producto
    fecha_fabricacion = models.DateTimeField()         # Fecha de fabricación del producto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)   # Relación con una categoría (si se elimina la categoría, se eliminan sus productos)


    def __str__(self):
        return self.nombre                             # Representación legible del producto


# Modelo para representar una venta
class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Producto vendido (si se elimina el producto, se elimina la venta)
    cantidad_producto = models.IntegerField()          # Cantidad de productos vendidos
    fecha_venta = models.DateTimeField()               # Fecha en que se realizó la venta
    total_precio = models.FloatField()                 # Total en dinero de la venta

    def __str__(self):
         return f'Venta de {self.cantidad_producto} de {self.producto.nombre}'  
         # Representación legible de la venta
