from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Pokemons(models.Model):
    nombre=models.CharField(max_length=30)
    numero=models.IntegerField()
    tipo1=models.CharField(max_length=30)
    tipo2=models.CharField(max_length=30)
    imagen = models.ImageField(null=True, blank=True)
    habilidad=models.CharField(max_length=30)
    debilidad=models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre:{self.nombre} - numero:{self.numero}"
  
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatar/', null=True, blank=True)
