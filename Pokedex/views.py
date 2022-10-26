from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

import datetime

from .models import *
from .forms import *

# Create your views here.


def home(request):
    last_pokemons = Pokemons.objects.order_by('-id')[0:3] 
    return render(request, "home.html", {"last_pokemons":last_pokemons})


def about(request):
    return render(request, "about.html")



def register(request):
    return render(request, "register.html")


def pokemons(request):
        pokemons = Pokemons.objects.all().order_by('numero')

        return render(request, "pokemons.html", {"pokemons":pokemons})

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

    return render(request, "login.html", {"form": form})


def logout_request(request):
    logout(request)
    return redirect("login")


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

        return render(request, 'register.html', {"form": form})

    form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


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

            messages.success(request, "Profile successfully updated")
            return redirect('editar_perfil')

    else:
        form = UserEditForm(initial={'email': user.email, "first_name": user.first_name, "last_name": user.last_name})

    return render(request, 'edit_user.html', {"form": form})


@login_required
def agregar_avatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = request.user

            avatar = Avatar(user=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            messages.success(request, "Profile updated successfully") 
            return redirect("editar_perfil")

    else:

        form = AvatarForm()

    
    return render(request, "add_avatar.html", {"form":form})

class cambiar_password(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy('editar_perfil') 

    def get_context_data(self, *args, **kwargs):
        contexto = super(cambiar_password, self).get_context_data()
        mensaje = messages.success(self.request, "Password updated successfully")

        contexto['mensaje']=mensaje

        return contexto

@login_required
def create_pokemon(request):   
   
    if request.method == "POST":
        
        pokemon = CreatePokemon(request.POST, request.FILES)
        
        if pokemon.is_valid():

            info = pokemon.cleaned_data

            new_pokemon = Pokemons(numero=info["numero"],nombre=info["nombre"],tipo1=info["tipo1"],tipo2=info["tipo2"],habilidad=info["habilidad"],debilidad=info["debilidad"],imagen=info["imagen"],descripcion=info["descripcion"], fecha=datetime.datetime.today(), autor=request.user)
            new_pokemon.save()

            messages.success(request, "Pokemon added successfully") 
            return redirect('my_pokemons')
        
        return render(request, "createpokemon", {"pokemon":pokemon})
    
    pokemon = CreatePokemon()
    return render(request, 'createpokemon.html', {'pokemon':pokemon})

@login_required
def my_pokemons(request):
    pokemons = Pokemons.objects.filter(autor=request.user).order_by('numero')        

    return render(request, "my_pokemons.html", {"pokemons":pokemons})

class draw_pokemon(DetailView):

    model = Pokemons
    template_name = "draw_pokemon.html"  

    def get_context_data(self, *args, **kwargs):
        contexto = super(draw_pokemon, self).get_context_data()

        #publicacion = get_object_or_404(Pokemons, id=self.kwargs['pk'])
        #total_likes = publicacion.total_likes()
        #contexto['total_likes'] = total_likes

        return contexto


@login_required
def edit_pokemon(request, pokemon_id):
    
    pokemon = Pokemons.objects.get(id=pokemon_id)

    if request.method == "POST":

        formulario = CreatePokemon(request.POST, request.FILES)

        if formulario.is_valid():

            info_pokemon = formulario.cleaned_data

            pokemon.numero = info_pokemon["numero"]
            pokemon.nombre = info_pokemon["nombre"]
            pokemon.tipo1 = info_pokemon["tipo1"]
            pokemon.tipo2 = info_pokemon["tipo2"]
            pokemon.habilidad = info_pokemon["habilidad"]
            pokemon.debilidad = info_pokemon["debilidad"]
            pokemon.imagen = info_pokemon["imagen"] 
            pokemon.descripcion = info_pokemon["descripcion"]        

            pokemon.save()
            messages.success(request, "Pokemon edited successfully") 
            
            return redirect ("my_pokemons")

    formulario = CreatePokemon(initial={"numero":pokemon.numero, "nombre":pokemon.nombre, "tipo1":pokemon.tipo1, "tipo2":pokemon.tipo2, "habilidad":pokemon.habilidad, "debilidad":pokemon.debilidad, "descripcion":pokemon.descripcion, "fecha":datetime.datetime.today()})

    return render (request, "edit_pokemon.html", {"form":formulario})

@login_required
def delete_pokemon(request, pokemon_id):

    pokemon = Pokemons.objects.get(id=pokemon_id)
    pokemon.delete()

    messages.success(request, "Pokemon deleted successfully.") 
    return redirect("my_pokemons")

