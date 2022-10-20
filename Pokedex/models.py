from django.db import models

# Create your models here.

class Pokemons(models.Model):
    nombre=models.CharField(max_length=30)
    numero=models.IntegerField()
    tipo1=models.CharField(max_length=30)
    tipo2=models.CharField(max_length=30)
    imagen = models.ImageField(null=True, blank=True)
    habilidad=models.CharField(max_length=30)
    debilidad=models.CharField(max_length=30)
  
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    email= models.EmailField()