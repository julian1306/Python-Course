from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from productos.models import Procutos

# Create your views here.

# Plantilla que crea un producto le manda como producto_nuevo y producto all al HTML producto nuevo asi te muestra el que va a crear y todo en un for . 
def producto(request):
    producto_nuevo = Procutos.objects.create(
        name = "AMD Ryzen 2600",
        price = 250,
        description = "CPU AMD RYZEN 2600 4 Ghz",
        SKU = "KHKTK15165",
        available = True
        )
    productos_all = Procutos.objects.all()    
    context = {"producto_nuevo":producto_nuevo, "productos_all":productos_all}
    return render(request, "crear_producto_nuevo.html", context = context)


# Plantilla para mandar todo al HTML productos ( productos.html)

def productos_all(request):

    productos_all = Procutos.objects.all()    
    context = {"productos_all":productos_all}

    return render(request, "listar_productos.html", context = context)