from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("signup/", views.signup, name = "signup"),
    path("login123/", views.login123, name = "login123"),
    path("vista_producto/<int:products_id>/", views.vistadelproducto, name="vista_producto"),
    path("carrito/", views.carrito, name = "carrito"),
    path("agregar/<int:producto_id>/", views.agregar_producto, name = "agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name = "eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name = "restar"),
    path("limpiar/<int:producto_id>/", views.limpiar_carro, name = "limpiar"),
    path('logout/', views.logout_view, name='logout'),
    path("contacto/", views.contacto, name = "contacto" ),
    path("about/", views.about, name = "about" )
]
