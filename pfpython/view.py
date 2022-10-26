from django.http import HttpResponse
from django.template import loader

from Pokedex.views import *

def home(request):
    last_pokemons = Pokemons.objects.order_by('-id')[0:3] 
    return render(request, "home.html", {"last_pokemons":last_pokemons})