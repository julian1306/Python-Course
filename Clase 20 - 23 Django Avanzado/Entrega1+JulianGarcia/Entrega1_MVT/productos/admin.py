from django.contrib import admin
from productos.models import Productos, Productos_herramientas, Productos_muebles, Contacto

# Register your models here.

admin.site.register(Productos)
admin.site.register(Productos_herramientas)    
admin.site.register(Productos_muebles)
admin.site.register(Contacto)  

