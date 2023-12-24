from django.contrib import admin
from .models import Products, Valoracion, contacto

# Register your models here.

admin.site.register(Products)
admin.site.register(Valoracion)
admin.site.register(contacto)