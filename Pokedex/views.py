from django.contrib import messages
from tkinter.messagebox import RETRY
from tokenize import Number
from unicodedata import name
from unittest import loader
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Pokedex.models import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
import datetime
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


##def login(request):
##    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def pokemon(request):
    if request.method == "POST":
        pokemon = Pokemons(nombre=request.POST["nombre"], numero=request.POST["numero"], tipo1=request.POST["tipo1"],
                           tipo2=request.POST["tipo2"], habilidad=request.POST["habilidad"], debilidad=request.POST["debilidad"],  imagen=request.POST["imagen"])
        pokemon.save()
        return render(request, "home.html")
    return render(request, "pokemon.html")


def buscar_pokemon(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        pokemons = Pokemons.objects.filter(nombre__icontains=nombre)
        return render(request, "pokemon.html", {"pokemons": pokemons})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)                
                return redirect("home")
            else:                
                return redirect("login")
                
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"login.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("home")   

def registro(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')            
            else:
                return redirect('login')
        
        return render(request, 'register.html', {"form":form})
    
    form = UserRegisterForm()
    return render(request, 'register.html', {"form":form})

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == "POST":

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']                                

            user.save()

            messages.success(request, "Los cambios fueron actualizados.") 
            return redirect('editar_perfil')

    else:
        form = UserEditForm(initial={'email':user.email, "first_name":user.first_name, "last_name":user.last_name})
    
    return render (request, 'edit_user.html', {"form":form})

@login_required
def agregar_avatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = request.user

            avatar = Avatar(user=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            messages.success(request, "El avatar se agrego exitosamente.") 
            return redirect("home")

    else:

        form = AvatarForm()

    
    return render(request, "add_avatar.html", {"form":form})

class cambiar_password(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy('editar_perfil') 

    def get_context_data(self, *args, **kwargs):
        contexto = super(cambiar_password, self).get_context_data()
        mensaje = messages.success(self.request, 'La contraseña se cambio correctamente')

        contexto['mensaje']=mensaje

        return contexto    