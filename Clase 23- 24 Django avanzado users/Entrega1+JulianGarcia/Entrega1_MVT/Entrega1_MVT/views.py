# Create views in directory root 

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
from productos.models import Productos,Productos_herramientas,Productos_muebles,Contacto
from productos.forms import Contacto_form



# Ofertas index.html 

def ofertas(request):
    search_products_herramientas = Productos_herramientas.objects.filter(clase = "Hogar")
    search_products_muebles = Productos_muebles.objects.filter(tipo = "Hogar")
    if search_products_herramientas.exists() or search_products_muebles.exists():
        context = {"search_products_herramientas":search_products_herramientas,"search_products_muebles":search_products_muebles}
    else:
        context = {'errors_herramientas': f'Disculpe, no se encontro herramientas en oferta','errors_muebles': f'Disculpe, no se encontro muebles en oferta'}         
    return render(request, 'index.html', context = context)  



def contacto(request):
    if request.method == "GET":
        form = Contacto_form()
        context = {"form":form}
        return render(request, "create_contact.html", context=context)
    else:
        form = Contacto_form(request.POST)
        if form.is_valid():
            new_contact = Contacto.objects.create(
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            email = form.cleaned_data['email'],
            )
            context = {"new_contact":new_contact}

        return render(request, "create_contact.html", context=context)  