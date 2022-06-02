from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from productos.models import Productos
from productos.forms import Product_form    # Aca importo el formulario 

# Create your views here.


# Plantilla para mandar todo al HTML productos ( productos.html)

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
        form = Product_form(request.POST)
        if form.is_valid():
            new_product = Productos.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                available = form.cleaned_data['available'],
            )
            context = {"new_product":new_product}
        return render(request, "create_product.html", context=context)    

    