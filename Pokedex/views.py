from tkinter.messagebox import RETRY
from tokenize import Number
from unicodedata import name
from unittest import loader
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
from Pokedex.models import Pokemons, Usuarios

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
