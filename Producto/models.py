from django.db import models

# Modelo que representa una categoría para clasificar productos.
class Categoria(models.Model):
    # Nombre identificativo de la categoría, con un máximo de 50 caracteres.
    nombre = models.CharField(max_length=50)

    # Breve descripción de la categoría, también hasta 50 caracteres.
    descripcion = models.CharField(max_length=50)

    # Representación textual que devuelve el nombre al mostrar un objeto Categoria.
    def __str__(self):
        return self.nombre


# Modelo que almacena información sobre un producto específico.
class Producto(models.Model):
    # Nombre del producto, hasta 50 caracteres.
    nombre = models.CharField(max_length=50)

    # Descripción detallada del producto, permitiendo hasta 60 caracteres.
    descripcion = models.CharField(max_length=60)

    # Cantidad disponible en stock, representada como número entero.
    stock = models.IntegerField()

    # Precio unitario del producto, guardado como número decimal flotante.
    precio = models.FloatField()

    # Fecha y hora en que el producto vence o deja de ser válido.
    fecha_vencimiento = models.DateTimeField()

    # Fecha y hora en que el producto fue fabricado.
    fecha_fabricacion = models.DateTimeField()

    # Relación con la categoría a la que pertenece el producto.
    # Si se elimina la categoría, se eliminan también sus productos.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Devuelve el nombre del producto al representarlo en texto.
    def __str__(self):
        return self.nombre


# Modelo que registra una venta realizada de un producto.
class Venta(models.Model):
    # Producto vendido, relacionado mediante clave foránea.
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    # Cantidad del producto vendida en esta transacción.
    cantidad_producto = models.IntegerField()

    # Fecha y hora en que se realizó la venta.
    fecha_venta = models.DateTimeField()

    # Precio total pagado por la venta (cantidad * precio unitario).
    total_precio = models.FloatField()

    # Representación textual que indica la cantidad vendida y el nombre del producto.
    def __str__(self):
         return f'Venta de {self.cantidad_producto} de {self.producto.nombre}'

