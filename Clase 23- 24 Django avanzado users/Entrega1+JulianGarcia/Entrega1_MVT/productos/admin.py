from django.contrib import admin
from productos.models import Productos, Productos_herramientas, Productos_muebles, Contacto, Categoria

# Register your models here.

#admin.site.register(Productos)
#admin.site.register(Productos_herramientas)    
#admin.site.register(Productos_muebles)
#admin.site.register(Contacto)  


@admin.register(Categoria)   # Nueva forma de registrarlo 
class CategoriaAdmin(admin.ModelAdmin):  # forma para que te muestre lo que quieras en el admin site 
    list_display = ["name", "description"] 


@admin.register(Productos)   # Nueva forma de registrarlo 
class ProductosAdmin(admin.ModelAdmin):  # forma para que te muestre lo que quieras en el admin site 
    list_display = ["name", "price", "SKU", "available"] 


@admin.register(Productos_herramientas)   # Nueva forma de registrarlo 
class Productos_herramientasAdmin(admin.ModelAdmin):  # forma para que te muestre lo que quieras en el admin site 
    list_display = ["name", "price", "SKU", "available","energia","clase"] 

@admin.register(Productos_muebles)   # Nueva forma de registrarlo 
class Productos_mueblesAdmin(admin.ModelAdmin):  # forma para que te muestre lo que quieras en el admin site 
    list_display = ["name", "price", "SKU", "available","tipo","capacidad"]


@admin.register(Contacto)   # Nueva forma de registrarlo 
class ContactoAdmin(admin.ModelAdmin):  # forma para que te muestre lo que quieras en el admin site 
    list_display = ["nombre", "apellido", "email"]      


