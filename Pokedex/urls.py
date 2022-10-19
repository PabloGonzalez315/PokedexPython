from django.urls import path
from django.views import *
from Pokedex.views import *

urlpatterns = [
    path("home/", home),
    path("about/", about),
    path("login/", login),
    path("register/", register),
    
]

