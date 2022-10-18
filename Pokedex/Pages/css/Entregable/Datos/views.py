from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Datos.models import Familia

# Create your views here.

def datosFam(self):
    Fam = Familia.objects.all()
    data = {'Fam':Fam}
    planilla = loader.get_template('familia.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

