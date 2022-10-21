from django.urls import path
from django.views import *
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
    path('editarperfil/password', cambiar_password.as_view(template_name='MillasViajerasApp/cambiar_pass.html'), name='cambiar_pass'),
    path("pokemon/", pokemon),
    path("buscar_pokemon/", buscar_pokemon),
]

