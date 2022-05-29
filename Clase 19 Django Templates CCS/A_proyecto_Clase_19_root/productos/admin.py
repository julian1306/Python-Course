from django.contrib import admin
from productos.models import Procutos # Aca le hago import de la clase/ modelo Productos
# Register your models here.

admin.site.register(Procutos)   # Aca registro los productos para laburarlos del portal de admin


