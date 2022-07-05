# Create views in directory root 

from datetime import datetime
import re
from math import ceil
from django.forms import NullBooleanField
from django.http import HttpRequest
from django.shortcuts import redirect, render
from productos.models import Productos,Productos_herramientas,Productos_muebles,Contacto
from productos.forms import Contacto_form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm   ### Formulario para auth y registrer default django 
from django.contrib.auth import authenticate, login, logout     # verifica la auth y el login 
from Entrega1_MVT.forms import User_registration_form # registro custom 
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin  # para req de logeado
from django.views.generic import View, ListView, DetailView , CreateView, DeleteView , UpdateView
from django.contrib.auth.models import User  
from django.urls import reverse  
from django.contrib.auth.decorators import permission_required




#def registro 

def register_view(request):
    if request.method == "GET":                                 # si es por GET osea cuando apenas ingresa a la pag 
        form = User_registration_form()
        context = {"form":form}
        return render(request,"auth/register.html", context=context)

    elif request.method == "POST":                                      # si es post osea manda el formulario por post 
        form = User_registration_form(request.POST)           #le pasa la data al POST 
        if form.is_valid():
            form.save()                                 # Aca lo guarda 
            #Aca lo logea 
            username = form.cleaned_data["username"] 
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            errors = form.errors                         # te tira los errores del formulario 
            form = User_registration_form()                  #traigo el form de vuelta  
            context = {'errors':errors, 'form':form}          # le mando los errores y el form de nuevo para que intente logear 
            return render(request, 'auth/login.html', context = context)                                                

# def para login 

def login_view(request):  

    if request.method == "GET":                                 # si es por GET osea cuando apenas ingresa a la pag 
        form = AuthenticationForm() # formulario importado linea 8
        context = {"form":form}
        return render(request,"auth/login.html", context=context)
    
    elif request.method == "POST":                  # si es post osea manda el formulario por post 
        form = AuthenticationForm(request, data = request.POST) #le pasa la data al POST 
        
        if form.is_valid():
            username = form.cleaned_data["username"] # agarra la info que el se cargo en el formulario y le asigna la variable username 
            password = form.cleaned_data["password"] # agarra la pass del form y le asig la variable password 
            user = authenticate(username=username, password=password) # aca el authenticate compara y te devuelve el user
            login(request, user)             #Logea a ese usuario
            next = request.GET.get('next')               ## !!!!! Clave para que lo mande a la pagina de donde venia next
            if next:                                    # if por si existe el next para no romper el login normal 
                return redirect(next)                             # aca lo mando por donde venia 
            else:
                return redirect("index")     # lo redirecciono al index  
        else:
            errors = form.errors                         # te tira los errores del formulario 
            form = AuthenticationForm()                  #traigo el form de vuelta  
            context = {'errors':errors, 'form':form}          # le mando los errores y el form de nuevo para que intente logear 
            return render(request, 'auth/login.html', context = context)
    else: 
        pass

# Para logout 

def logout_view(request):
    logout(request)
    return redirect("index")



# Ofertas index.html 



def index(request):
    print(request.user)                                 # para saber el user 
    print(request.user.is_authenticated)                # para saner si el user esta auth 
    #if request.user.is_authenticated:
            #print(request.user.user_profile.id)
    print(request.user.id)                   # me tira el perfil del usuario 


    username = request.user                    # aca para que saque el user que esta logeado y lo pueda mostra en el context con un "message"


    if request.user.is_authenticated:
        if request.user.level == 5 :
            for product in Productos.objects.filter(available=True):
                multiplier = 50/100                   # 50% 
                old_price = product.price
                product.new_price = ceil(old_price - (old_price * multiplier))
                product.save(update_fields=['new_price'])
                print(product.name, product.price, product.new_price)
        elif request.user.level == 4:
            for product in Productos.objects.filter(available=True):
                multiplier = 40/100                   # 40% 
                old_price = product.price
                product.new_price = ceil(old_price - (old_price * multiplier))
                product.save(update_fields=['new_price'])
                print(product.name, product.price, product.new_price)
        elif request.user.level == 3:
            for product in Productos.objects.filter(available=True):
                multiplier = 30/100                   # 30% 
                old_price = product.price
                product.new_price = ceil(old_price - (old_price * multiplier))
                product.save(update_fields=['new_price'])
                print(product.name, product.price, product.new_price)
        elif request.user.level == 2:
            for product in Productos.objects.filter(available=True):
                multiplier = 20/100                   # 30% 
                old_price = product.price
                product.new_price = ceil(old_price - (old_price * multiplier))
                product.save(update_fields=['new_price'])
                print(product.name, product.price, product.new_price)
        else:
            for product in Productos.objects.filter(available=True):
                product.new_price = 0                                         # Ver como pasarlo a null convierte a 0 ok 
                product.save(update_fields=['new_price'])
                print("brian", product.name, product.price, product.new_price)
    else:
        for product in Productos.objects.filter(available=True):
            product.new_price = 0                                         # Ver como pasarlo a null convierte a 0 ok 
            product.save(update_fields=['new_price'])
            print("brian", product.name, product.price, product.new_price)



    #Ofertas general index 
    #OFertas de articulos Hogar
    search_products_herramientas = Productos_herramientas.objects.filter(clase = "Hogar")
    search_products_muebles = Productos_muebles.objects.filter(tipo = "Hogar")

    if search_products_herramientas.exists() or search_products_muebles.exists():
        context = {"bienvenida": f"Bienvenido {username}","search_products_herramientas":search_products_herramientas,"search_products_muebles":search_products_muebles}
    else:
        context = {"bienvenida": f"Bienvenido {username}",'errors_herramientas': f'Disculpe, no se encontro herramientas en oferta','errors_muebles': f'Disculpe, no se encontro muebles en oferta'}       
    
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





def about_us(request):
    print(request.user)

    context = {"algo": "algo"}
    return render(request, "about_us.html", context=context)