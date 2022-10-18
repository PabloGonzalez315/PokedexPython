from django.db import models

# Create your models here.

class Familia(models.Model):
    Nombre=models.CharField(max_length=40)
    Apellido=models.CharField(max_length=40)
    Edad=models.IntegerField()
    Dni=models.IntegerField()
