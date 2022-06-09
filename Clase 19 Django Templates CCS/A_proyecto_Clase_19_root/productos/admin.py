from django.contrib import admin
from productos.models import Productos # Aca le hago import de la clase/ modelo Productos



# Register your models here.

#admin.site.register(Productos)   # Aca registro los productos para laburarlos del portal de admin

@admin.register(Productos)   # Nueva forma de registrarlo 
class ProductosAdmin(admin.ModelAdmin):  # forma para que te muestre lo que quieras en el admin site 
    list_display = ["name", "price", "SKU", "available"] 


