# Create views in directory root 

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render 


def index(request):                                    # Aca creo una def para la pagina de inicio 
    return render(request, "index.html")               # con esto se lo mando al index.html el template para esta pagina de inicio en carpeta templates 

