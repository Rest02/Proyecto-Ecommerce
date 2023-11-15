from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login123(request):
    return render(request, "login123.html")


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