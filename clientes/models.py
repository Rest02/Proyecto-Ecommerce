from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    cantidad_disponible = models.IntegerField(default=0)
    nombre_producto = models.CharField(max_length=200)
    precio_producto = models.IntegerField(default=0)
    descripcion_producto = models.TextField()
    image = models.ImageField(blank=True, null=True)
    categoria = models.CharField(max_length=100, default="Producto")

    def __str__(self):
        return self.nombre_producto
    
class Valoracion(models.Model):
    producto = models.ForeignKey(Products, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return self.comentario + " - " + self.producto.nombre_producto
    

class contacto(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    asunto = models.CharField(max_length=200)
    telefono = models.IntegerField(max_length=9)
    mensaje = models.TextField()

    def __str__(self):
        return self.user.username + " - " + self.asunto