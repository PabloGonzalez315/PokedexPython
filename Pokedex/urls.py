from django.urls import path
from django.views import *
from Pokedex.views import *

urlpatterns = [
    path("home/", home),
    path("about/", about),
    path("login/", login),
    path("register/", register),
    path("pokemon/", pokemon),
    path("buscar_pokemon/", buscar_pokemon),
    path('create_pokemons/', create_pokemons),
    path('read_pokemons/', read_pokemons),
    path('update_pokemons/<pokemon_id>', update_pokemons),
    path('delete_pokemons/<pokemon_id>', delete_pokemons),
    
]

