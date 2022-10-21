from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from Pokedex.models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar", widget=forms.PasswordInput)
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}
        
class UserEditForm(forms.Form):

    email = forms.EmailField(label="Email")  
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")    
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']        