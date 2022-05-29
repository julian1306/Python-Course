from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from familiares.models import Familiares


# Create your views here.

def familiares(request):
    familiares_all = Familiares.objects.all()


    context = { "familiar_nuevo":familiar_nuevo, "familiar_nuevo2":familiar_nuevo2, "familiar_nuevo3":familiar_nuevo3, "familiares_all":familiares_all}
    return render(request, "familiares.html", context)


    