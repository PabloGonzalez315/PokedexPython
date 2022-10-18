from turtle import width
from django.db import models

# Create your models here.

class Pokemon(models.Model):
    number=models.IntegerField(max_length=4)
    name=models.CharField(max_length=30)
    type1=models.CharField(max_length=30)
    type2=models.CharField(max_length=30)
    width=models.IntegerField()
    height=models.IntegerField()
    ability=models.CharField(max_length=30)
    weak=models.CharField(max_length=30)
    prevolution=models.CharField(max_length=30)
    evolution=models.CharField(max_length=30)
    region=models.CharField(max_length=30)
    description=models.CharField(max_length=300)
    