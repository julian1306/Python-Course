# Create views in directory root 

from datetime import datetime
import re
from django.http import HttpRequest
from django.shortcuts import redirect, render
from productos.models import Productos,Productos_herramientas,Productos_muebles,Contacto
from productos.forms import Contacto_form
from django.contrib.auth.forms import AuthenticationForm   ### Formulario para auth
from django.contrib.auth import authenticate, login     # verifica la auth y el login 

# def oara login 

def login_view(request):
    
    
    
    
    if request.method == "POST":                  # si es post osea manda el formulario por post 
        form = AuthenticationForm(request, data = request.POST) #le pasa la data al POST 
        
        if form.is_valid():
            username = form.cleaned_data["username"] # agarra la info que el se cargo en el formulario y le asigna la variable username 
            password = form.cleaned_data["password"] # agarra la pass del form y le asig la variable password 
            user = authenticate(username=username, password=password) # aca el authenticate compara y te devuelve el user
            login(request, user)             #Logea a ese usuario 
            context= {"message": f"bienvenido {username}"}
            return redirect("index")                         # lo redirecciono al index      
        else:
            errors = form.errors                         # te tira los errores del formulario 
            form = AuthenticationForm()                  #traigo el form de vuelta  
            context = {'errors':errors, 'form':form}          # le mando los errores y el form de nuevo para que intente logear 
            return render(request, 'auth/login.html', context = context)

    else:                                        # si es por GET osea cuando apenas ingresa a la pag 
        form = AuthenticationForm() # formulario importado linea 8
        context = {"form":form}
        return render(request,"auth/login.html", context=context)






# Ofertas index.html 



def index(request):
    print(request.user)                                 # para saber el user 
    print(request.user.is_authenticated)                # para saner si el user esta auth 


    username = request.user                      # aca para que saque el user que esta logeado y lo pueda mostra en el context con un "message"

    #Ofertas general index 

    search_products_herramientas = Productos_herramientas.objects.filter(clase = "Hogar")
    search_products_muebles = Productos_muebles.objects.filter(tipo = "Hogar")

    if search_products_herramientas.exists() or search_products_muebles.exists():
        context = {"message": f"Bienvenido {username}","search_products_herramientas":search_products_herramientas,"search_products_muebles":search_products_muebles}
    else:
        context = {"message": f"Bienvenido {username}",'errors_herramientas': f'Disculpe, no se encontro herramientas en oferta','errors_muebles': f'Disculpe, no se encontro muebles en oferta'}       
    
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