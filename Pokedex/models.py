from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pokemons(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField()
    tipo1 = models.CharField(max_length=30)
    tipo2 = models.CharField(max_length=30)
    imagen = models.CharField(max_length=400)
    habilidad = models.CharField(max_length=30)
    debilidad = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre:{self.nombre} - numero:{self.numero}"


class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    email = models.EmailField()


class Avatar(models.Model):
    # vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # subcarpeta Avatares de media
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
