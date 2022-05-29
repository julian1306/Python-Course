from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from familiares.models import Familiares


# Create your views here.

def familiares(request):
    familiar_nuevo = Familiares.objects.create(
        nombre = "Gabriel",
        apellido = "Garcia",
        edad = 60,
        dni = 17852974,
        fecha_nacimiento = "07/06/1962",
    )
    familiar_nuevo2 = Familiares.objects.create(
        nombre = "Veronica",
        apellido = "Salmoiraghi",
        edad = 57,
        dni = 119587634,
        fecha_nacimiento = "30/10/1971",
    )
    familiar_nuevo3 = Familiares.objects.create(
        nombre = "Nicolas",
        apellido = "Vivas",
        edad = 15,
        dni = 52635898,
        fecha_nacimiento = "15/08/2007",
    )
    familiares_all = Familiares.objects.all()


    context = { "familiar_nuevo":familiar_nuevo, "familiar_nuevo2":familiar_nuevo2, "familiar_nuevo3":familiar_nuevo3, "familiares_all":familiares_all}
    return render(request, "familiares.html", context)


    