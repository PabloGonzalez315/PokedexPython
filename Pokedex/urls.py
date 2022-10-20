from django.urls import path
from django.views import *
from Pokedex.views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("about/", about),
    path('login/', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path("register/", register),
    path("pokemon/", pokemon),
    path("buscar_pokemon/", buscar_pokemon),
]

