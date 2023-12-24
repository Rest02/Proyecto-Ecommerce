from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import Products, Valoracion
from .forms import ValoracionForm
from .carro import Carro
from .forms import ContactoForm
# from django.db.models import Q





# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')



def home(request):
    products = Products.objects.all()

    
    # Obtener parámetros de la URL
    categoria = request.GET.get('categoria')
    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    # Aplicar filtros si se proporcionan
    if categoria:
        products = products.filter(categoria=categoria)
    if nombre:
        products = products.filter(nombre_producto__icontains=nombre)
    if precio_min:
        products = products.filter(precio_producto__gte=precio_min)
    if precio_max:
        products = products.filter(precio_producto__lte=precio_max)

    return render(request, 'home.html', {"productos":products})



def login123(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        # Obtener los datos del formulario de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario se autenticó correctamente, iniciar sesión
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio después del inicio de sesión
        else:
            # El usuario no se autenticó correctamente, manejar el error
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'login123.html', {'form': form})


def signup(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('login123')
        else:
            data['form'] = user_creation_form

    return render(request, 'signup.html', data)


def vistadelproducto(request, products_id):
    producto_seleccionado = get_object_or_404(Products, pk=products_id)
    valoraciones_filtradas = Valoracion.objects.filter(producto=producto_seleccionado)
    form = ValoracionForm()

    if request.method == 'POST':
        form = ValoracionForm(request.POST)
        if form.is_valid():
            valoracion = form.save(commit=False)
            valoracion.producto = producto_seleccionado
            valoracion.usuario = request.user  # Suponiendo que tienes un sistema de autenticación de usuarios
            valoracion.save()

    return render(request, 'vista_producto.html', {
        'producto': producto_seleccionado, 
        'valoraciones': valoraciones_filtradas, 
        'form': form
        })


def carrito(request):
    return render(request, "carrito.html" )



def agregar_producto(request, producto_id):

    carro = Carro(request)

    producto = Products.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("/carrito/")

def eliminar_producto(request, producto_id):

    carro = Carro(request)

    producto = Products.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("/carrito/")

def restar_producto(request, producto_id):

    carro = Carro(request)

    producto = Products.objects.get(id=producto_id)

    carro.restar(producto=producto)

    return redirect("/carrito/")

def limpiar_carro(request):

    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("/carrito/")




from django. core.mail import send_mail


def mandar_correo(username, asunto, mensaje, user_email):
    subject = f"{asunto}"
    body = f"¡Hola Josefa!\n\nNos ponemos en contacto contigo ya que el usuario {username} con el correo {user_email} subio el siguiente mensaje a tu pagina web.\n\n"
    recipient_list = ["rodriguez.bastidas.matias@gmail.com"]

    send_mail(subject, body + mensaje, user_email, recipient_list)


from django.urls import reverse


def contacto(request):
    contact_form = ContactoForm()

    if request.method == "POST":
        contact_form = ContactoForm(data=request.POST)

        if contact_form.is_valid():
            contacto = contact_form.save(commit=False)
            contacto.user = request.user
            user_email = contacto.user.email
            username = contacto.user.username
            asunto = request.POST["asunto"]
            mensaje = request.POST["mensaje"]
            
            mandar_correo(username, asunto , mensaje, user_email)
            contact_form.save()

            # Tengo que avisar que todo fue bien
            return redirect(reverse("contacto")+"?ok")
        else:
            # Tengo que generar un error
            return redirect(reverse("contacto")+"?error")

    return render(request, "contacto.html", {"ContactoForm" : contact_form })

   

def about(request):
    return render(request, "about.html")




















# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.http import HttpResponse


# # Create your views here.
# def home(request):
#     return render(request, "home.html")


# def signup(request):
    
#     if request.method == "GET":
#         return render(request, "signup.html", {
#         "form" : UserCreationForm
#         })
#     else:
#         if request.POST["password1"] == request.POST["password2"]:
#             try:
#                 # Reguster user
#                 user = User.objects.create_user(username = request.POST["username"], password= request.POST["password1"])
#                 user.save()
#                 return HttpResponse("User created successully")
#             except:
#                 return HttpResponse("El usuario ya existe")
#         return HttpResponse("Las contraseñas no coinciden")