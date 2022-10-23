from django.urls import path
from Pokedex.views import *
from django.contrib.auth import views as auth_views




urlpatterns = [
    path("home/", home, name="home"),
    path("about/", about),
    path('login/', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('register/', registro, name='registro'),
    path('edit_user/', editar_perfil, name='editar_perfil'),  
    path('edit_user/add_avatar', agregar_avatar, name='agregar_avatar'),
    path('edit_user/password', cambiar_password.as_view(template_name='change_pass.html'), name='change_pass'),
    path('pokemons', pokemons, name='pokemons'),
    path('pokemons/<pk>', draw_pokemon.as_view(), name='draw_pokemon'),
    path('createpokemon', create_pokemon, name='create_pokemon'),
    path('edit_pokemon/<pokemon_id>', edit_pokemon, name='edit_pokemon'),
    path('delete_pokemon/<pokemon_id>', delete_pokemon, name='delete_pokemon'),
    path('my_pokemons', my_pokemons, name='my_pokemons'),
]

