from django.db import models



# Create your models here.
# class Clientes(models.Models):
#     nombre = models.CharField(max_length=200)
#     nombre_usuario = models.CharField(max_length=200)
#     correo_electronico = models.CharField(  )


class Products(models.Model):
    cantidad_disponible = models.IntegerField(default=0)
    nombre_producto = models.CharField(max_length=200)
    precio_producto = models.IntegerField(default=0)
    descripcion_producto = models.TextField()

    def __str__(self):
        return self.nombre_producto