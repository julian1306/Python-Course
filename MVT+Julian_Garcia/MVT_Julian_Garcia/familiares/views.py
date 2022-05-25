from multiprocessing import context
from django.shortcuts import render
from familiares.models import Familiares
from datetime import datetime


# Create your views here.

def familiares(request):
    familiar_nuevo = Familiares.objects.create(
        nombre = "Gabriel",
        apellido = "Garcia",
        edad = 60,
        dni = 17852974,
    )
    familiar_nuevo2 = Familiares.objects.create(
        nombre = "Veronica",
        apellido = "Salmoiraghi",
        edad = 57,
        dni = 119587634,
    )
    familiar_nuevo3 = Familiares.objects.create(
        nombre = "Nicolas",
        apellido = "Vivas",
        edad = 15,
        dni = 52635898,
    )

    context = { "familiar_nuevo":familiar_nuevo, "familiar_nuevo2":familiar_nuevo2, "familiar_nuevo3":familiar_nuevo3}
    return render(request, "familiares.html", context=context)


   