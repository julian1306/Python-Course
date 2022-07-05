from genericpath import exists
from itertools import product
from multiprocessing import context
from unicodedata import name
from xml.dom.minidom import Document
from django.shortcuts import redirect, render
from productos.models import Productos, Productos_herramientas, Productos_muebles, Contacto
from productos.forms import Product_form, Herramientas_form, Muebles_form    # Aca importo el formulario 
from django.views.generic import ListView, DetailView , CreateView, DeleteView , UpdateView # Aca importamos para la list view para las class 
from django.urls import reverse  # para mandar a otra funcion se usa en linea 33 
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin # para req de logeado 
from django.contrib.auth.decorators import login_required          # decorador para pedir que tenga que estar logeado mas facil 

# Create your views here.

# Products all listar_productos.html 

# Permisos Custom para porductos 

class SecureView_producto(PermissionRequiredMixin):
    ...
    permission_required = ('productos.add_productos', 'productos.change_productos','productos.delete_productos','productos.view_productos')
    ...
    #Solo admin y brian tiene los permisos requeridos 



class Productos_all(ListView):  
    model = Productos
    template_name = "listar_productos.html"
    queryset = Productos.objects.filter(available = True) # para mostras si estan activos    
    

# Product_detail.html view para el detalle 

class Detail_product(DetailView):
    model= Productos
    template_name = "detail_product.html"

# View para create_product.html 

class Create_product(SecureView_producto,CreateView):            # para que tenga que estar logeado 
    model = Productos
    template_name = "create_product.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("detail_product",kwargs={'pk':self.object.pk} )  # Aca con el reverse llamando al html  con los kwargs le paso el pk de lo que creamos y muestra el detalle 

# Para borrar va a delete_product.html" 

class Delete_product(SecureView_producto,DeleteView):        
    model = Productos
    template_name = "delete_product.html"

    def get_success_url(self):
        return reverse("listar_productos") # Elimina y nos manda a todos los procutos 

# Nuevo para update_product.html

class Update_product(SecureView_producto,UpdateView):
    model = Productos
    template_name = 'update_product.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_product', kwargs = {'pk':self.object.pk}) # lo mando al url dle name detail_product con el id




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


## ver esto 


@login_required                               # Decorador para que tenga que estar logeado 
def create_herramientas(request):
    if request.user.is_staff:
        print("paso is auth")
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
    else:
        #para ver el path donde esta y despues mandarlo seguir  viendo como hacer y pasar el next a mano hay 
        #BORRAR DECORADOR SINO NO LLEGA ACA 
        path = request.get_full_path()
        next = "next"+"="+path
        print(next)
        return redirect("login")







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


@login_required  ###------------------ se puede usar el decorador para forzar que este logeado en  vez de los if manuales 
def create_muebles(request):
    if request.user.is_staff:
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
    else:
        return redirect("login") 
        #kwargs = {'pk':self.object.pk}






# Products all listar_productos.html 

# def productos_all(request):

#     productos_all = Productos.objects.all()    
#     context = {"productos_all":productos_all}

#     return render(request, "listar_productos.html" , context = context)





# Product_detail.html view para el detalle 

# def detail_product(request, pk):  # Aca le paso la request y el pk que es lo mismo que el id del producto 
#     try:
#         producto = Productos.objects.get(id=pk) # esto va asi para que con el get busque el pk/id , va con un try por si no encuenta nada 
#         context= {"producto":producto}
#         return render(request, "product_detail.html", context=context) # lo mando a product_detail.html
#     except:
#         context = {"error": "El producto no existe"}
#         return render(request, "product_detail.html", context=context)   # si hay error lo mando a lister_productos.html y muestra error






# Para borrar va a delete_product.html" 

# def delete_product(request, pk):
#     print(request.GET)
#     try:    
#         if request.method == "GET":
#             producto = Productos.objects.get(id=pk)
#             context= {"producto":producto}
#             return render(request, 'delete_product.html', context=context)
#         else:
#             producto = Productos.objects.get(id=pk)
#             producto.delete()
#             context = {"message":"producto eliminado correctamente"} 
#             return render(request, "delete_product.html", context = context ) # lo elimina y lo manod a listar_productos.html y le muestra el {{message}}
#     except:
#         context = {"errors": "El producto no existe"}
#         return render(request, "delete_product.html", context=context)  # si 



# View para create_product.html 

# def create_product(request):
#     if request.method == "GET":
#         form = Product_form()
#         context = {"form":form}
#         return render(request, "create_product.html", context=context)
#     else:
#         form = Product_form(request.POST, request.FILES) # LA concha de la lora aaca poner request.FILES para la imagen 
#         if form.is_valid():
#             new_product = Productos.objects.create(
#                 name = form.cleaned_data['name'],
#                 price = form.cleaned_data['price'],
#                 description = form.cleaned_data['description'],
#                 SKU = form.cleaned_data['SKU'],
#                 available = form.cleaned_data['available'],
#                 imagen = form.cleaned_data['imagen']
#             )
#             context = {"new_product":new_product}
#         return render(request, "create_product.html", context=context)    



