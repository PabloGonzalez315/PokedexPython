from tkinter.messagebox import RETRY
from tokenize import Number
from unicodedata import name
from unittest import loader
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
from Pokedex.models import Pokemons, Usuarios
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from Pokedex.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def pokemon(request):
    if request.method == "POST":
        pokemon = Pokemons(nombre=request.POST["nombre"], numero=request.POST["numero"], tipo1=request.POST["tipo1"],
                           tipo2=request.POST["tipo2"], habilidad=request.POST["habilidad"], debilidad=request.POST["debilidad"],  imagen=request.POST["imagen"])
        pokemon.save()
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        return render(request, 'home.html', {'avatar': avatar})
    return render(request, "pokemon.html")


def buscar_pokemon(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        pokemons = Pokemons.objects.filter(nombre__icontains=nombre)
        return render(request, "pokemon.html", {"pokemons": pokemons})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

def create_pokemons(request):
    if request.method == 'POST':
        pokemon = Pokemons(nombre = request.POST['nombre'], numero = request.POST['numero'], tipo1 = request.POST['tipo1'])
        pokemon.save()
        pokemons = Pokemons.objects.all()    
        return render(request, "pokemonsCrud/read_pokemon.html", {"pokemons": pokemons})
    return render(request, "pokemonsCrud/create_pokemon.html")

def read_pokemons(request=None):
    pokemons = Pokemons.objects.all() #Trae todo
    return render(request, "pokemonsCrud/read_pokemon.html", {"pokemons": pokemons})

def update_pokemons(request, pokemon_id):
    pokemon = Pokemons.objects.get(id = pokemon_id)

    if request.method == 'POST':
        formulario = form_pokemons(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            pokemon.nombre = informacion['nombre']
            pokemon.numero = informacion['apellido']
            pokemon.tipo1 = informacion['email']
            pokemon.save()
            pokemons = Pokemons.objects.all() #Trae todo
            return render(request, "pokemonsCrud/read_pokemon.html", {"pokemons": pokemons})
    else:
        formulario = form_pokemons(initial={'nombre': pokemon.nombre, 'numero': pokemon.numero, 'tipo1': pokemon.tipo1})
    return render(request,"pokemonsCrud/update_pokemon.html", {"formulario": formulario})

def delete_pokemons(request, pokemon_id):
    pokemon = Pokemons.objects.get(id =  pokemon_id)
    pokemon.delete()

    pokemons = Pokemons.objects.all()    
    return render(request, "pokemonsCrud/read_pokemon.html", {"pokemons": pokemons})