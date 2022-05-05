from django.shortcuts import render
from .models import Opskrift, Ingrediens


def opskrift(request, opskrift_id):
    opskr = Opskrift.objects.get(pk=opskrift_id)
    return render(request, 'opskrift.html', {'opskrift': opskr, })


def opskrifter(request):
    alle_opskrifter = Opskrift.objects.all()
    return render(request, 'opskrifter.html', {'opskrifter': alle_opskrifter})

def ingredienser(request):
    alle_ingredienser = Ingrediens.objects.all()
    return render(request, 'ingredienser.html', {'ingredienser': alle_ingredienser})


def index(request):
    return render(request, 'nav.html')
