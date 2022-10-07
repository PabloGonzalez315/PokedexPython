from django.http import HttpResponse
from django.template import loader

from Pokedex.views import *

def homepage(request):
    return render(request, "home.html")