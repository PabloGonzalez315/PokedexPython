<<<<<<< HEAD
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
=======
from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_pokemons(forms.Form):
    nombre = forms.CharField(max_length=30)
    numero = forms.CharField(max_length=30)
    tipo1 = forms.CharField(max_length=30)
    tipo2 = forms.CharField(max_length=30)
    habilidad = forms.CharField(max_length=30)
    debilidad = forms.CharField(max_length=30)
    imagen = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Old Password"}))
    new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "New password"}))
    new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirm new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()
>>>>>>> Pablo
