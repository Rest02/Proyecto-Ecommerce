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
    # puntuacion = models.IntegerField()
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
    

class Direccion(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True, null=True)
    codigo_postal = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=255,blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    comuna = models.CharField(max_length=255, blank=True, null=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    casa_depto= models.IntegerField()

    def __str__(self):
        return self.user.username +" - "+ str(self.codigo_postal)