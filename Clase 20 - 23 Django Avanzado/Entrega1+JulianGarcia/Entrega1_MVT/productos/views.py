from genericpath import exists
from itertools import product
from multiprocessing import context
from unicodedata import name
from xml.dom.minidom import Document
from django.shortcuts import render
from productos.models import Productos, Productos_herramientas, Productos_muebles, Contacto
from productos.forms import Product_form, Herramientas_form, Muebles_form    # Aca importo el formulario 

# Create your views here.




# Products all listar_productos.html 

def productos_all(request):

    productos_all = Productos.objects.all()    
    context = {"productos_all":productos_all}

    return render(request, "listar_productos.html", context = context)


# View para create_product.html 

def create_product(request):
    if request.method == "GET":
        form = Product_form()
        context = {"form":form}
        return render(request, "create_product.html", context=context)
    else:
        form = Product_form(request.POST, request.FILES) # LA concha de la lora aaca poner request.FILES para la imagen 
        if form.is_valid():
            new_product = Productos.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                available = form.cleaned_data['available'],
                imagen = form.cleaned_data['imagen']
            )
            context = {"new_product":new_product}
        return render(request, "create_product.html", context=context)    



# View para el seach_product.html

def search_product(request):
    print(request.GET) # ACA LACE PRINT DEL GET QUE LLEGA 
    search_products = Productos.objects.filter(name__contains = request.GET["search"])
    if search_products.exists():
        context = {"search_products":search_products}
    else:
        context = {'errors': f'Disculpe, no se encontro el producto deseado'} 
    return render(request, 'search_product.html', context = context)    



##################################  / Herramientas ###############################    

def listar_herramientas(request):

    herramientas_all = Productos_herramientas.objects.all()    
    context = {"herramientas_all":herramientas_all}

    return render(request, "listar_herramientas.html", context = context)



def search_herramientas(request):
    print(request.GET) # ACA LACE PRINT DEL GET QUE LLEGA 
    #product = Productos.objects.get --- Busca de a una coincidencia
    search_products = Productos_herramientas.objects.filter(name__contains = request.GET["search"])  # comando para las busquedas es asi no lo pienses mucho 
    if search_products.exists():
        context = {"search_products":search_products}
    else:
        context = {'errors': f'Disculpe, no se encontro la herramienta deseada'} 
    return render(request, 'search_herramientas.html', context = context)  



def create_herramientas(request):
    if request.method == "GET":
        form = Herramientas_form()
        context = {"form":form}
        return render(request, "create_herramientas.html", context=context)
    else:
        form = Herramientas_form(request.POST, request.FILES) # LA concha de la lora aaca poner request.FILES para la imagen 
        if form.is_valid():
            new_product = Productos_herramientas.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                available = form.cleaned_data['available'],
                imagen = form.cleaned_data['imagen'],
                energia = form.cleaned_data['energia'],
                clase = form.cleaned_data['clase'],
            )
            context = {"new_product":new_product}
        return render(request, "create_herramientas.html", context=context)    








######################## / Muebles ######################################### 


def listar_muebles(request):

    muebles_all = Productos_muebles.objects.all()    
    context = {"muebles_all":muebles_all}

    return render(request, "listar_muebles.html", context = context)




def search_muebles(request):
    print(request.GET) # ACA LACE PRINT DEL GET QUE LLEGA 
    #product = Productos.objects.get --- Busca de a una coincidencia
    search_products = Productos_muebles.objects.filter(name__contains = request.GET["search"])  # comando para las busquedas es asi no lo pienses mucho 
    if search_products.exists():
        context = {"search_products":search_products}
    else:
        context = {'errors': f'Disculpe, no se encontro el mueble deseado'} 
    return render(request, 'search_muebles.html', context = context)    



def create_muebles(request):
    if request.method == "GET":
        form = Muebles_form()
        context = {"form":form}
        return render(request, "create_muebles.html", context=context)
    else:
        form = Muebles_form(request.POST, request.FILES) # LA concha de la lora aaca poner request.FILES para la imagen 
        if form.is_valid():
            new_product = Productos_muebles.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                available = form.cleaned_data['available'],
                imagen = form.cleaned_data['imagen'],
                tipo = form.cleaned_data['tipo'],
                capacidad = form.cleaned_data['capacidad'],
            )
            context = {"new_product":new_product}
        return render(request, "create_muebles.html", context=context)    
