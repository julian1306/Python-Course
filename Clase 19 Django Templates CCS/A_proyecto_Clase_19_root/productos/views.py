from itertools import product
from multiprocessing import context
from unicodedata import name
from xml.dom.minidom import Document
from django.shortcuts import render
from productos.models import Productos
from productos.forms import Product_form    # Aca importo el formulario 

# Create your views here.


# Plantilla para mandar todo al HTML productos ( productos.html)

def productos_all(request):

    productos_all = Productos.objects.all()    
    context = {"productos_all":productos_all}

    return render(request, "listar_productos.html", context = context)


# Product_detail.html view para el detalle 

def detail_product(request, pk):  # Aca le paso la request y el pk que es lo mismo que el id del producto 
    try:
        producto = Productos.objects.get(id=pk) # esto va asi para que con el get busque el pk/id , va con un try por si no encuenta nada 
        context= {"producto":producto}
        return render(request, "product_detail.html", context=context)
    except:
        context = {"error": "El producto no existe"}
        return render(request, "product_detail.html", context=context)  









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

    

def search_product(request):
    print(request.GET) # ACA LACE PRINT DEL GET QUE LLEGA 
    #product = Productos.objects.get --- Busca de a una coincidencia
    search_products = Productos.objects.filter(name__contains = request.GET["search"])  # comando para las busquedas es asi no lo pienses mucho 

    context = {"search_products":search_products}

    return render(request, "search_product.html", context=context)   