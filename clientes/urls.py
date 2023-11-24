from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("signup/", views.signup, name = "signup"),
    path("login123/", views.login123, name = "login123"),
    path("vista_producto/<int:products_id>/", views.vistadelproducto, name="vista_producto")
]
