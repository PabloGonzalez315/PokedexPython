from turtle import width
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pokemon(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=30)
    type1=models.CharField(max_length=30)
    type2=models.CharField(max_length=30)
    ability=models.CharField(max_length=30)
    weak=models.CharField(max_length=30)
    description=models.CharField(max_length=300)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatar/', null=True, blank=True)

