from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Valoracion, contacto, Direccion

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email
	
# forms.py



class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['comentario']


class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ['asunto', 'telefono', "mensaje"]

class PerfilForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']
        
        
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ["codigo_postal", "region", "ciudad" , "comuna", "calle" , "casa_depto"]
        widgets = {
            'codigo_postal': forms.TextInput(attrs={'placeholder': '325689'}),
            'region': forms.TextInput(attrs={'placeholder': 'region'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'ciudad'}),
            'comuna': forms.TextInput(attrs={'placeholder': 'comuna'}),
            'calle': forms.TextInput(attrs={'placeholder': 'calle'}),
            'casa_depto': forms.TextInput(attrs={'placeholder': '11'}),
        }