from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Pokemons(models.Model):
    nombre=models.CharField(max_length=30)
    numero=models.IntegerField()
    tipo1=models.CharField(max_length=30)
    tipo2=models.CharField(max_length=30)
    imagen = models.ImageField(null=True, blank=True)
    habilidad=models.CharField(max_length=30)
    debilidad=models.CharField(max_length=30)
    descripcion = RichTextField(blank=True, null=True)
    fecha = models.DateField(null=True)
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Pokemons"
    
    def __str__(self):
        return '%s - %s' % (self.nombre, self.autor)
  
class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatar/', null=True, blank=True)
