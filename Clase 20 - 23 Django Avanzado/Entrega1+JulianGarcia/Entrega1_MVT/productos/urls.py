
#URLS dentro de http://127.0.0.1:8000/productos/

from django.urls import path, include
from productos.views import productos_all,create_product, search_product,listar_herramientas,search_herramientas,create_herramientas,listar_muebles, search_muebles, create_muebles




urlpatterns = [
    
    path("listar_productos/", productos_all , name = "listar_productos"),
    path("crear_productos/", create_product, name="crear_productos"),  # Aca creo las urls de products y llamo a las views de product 
    path("buscar_productos/", search_product, name = "buscar_productos"),
    path("herramientas/listar_herramientas/", listar_herramientas, name="listar_herramientas"),
    path("herramientas/search_herramientas/", search_herramientas, name="search_herramientas"),
    path("herramientas/create_herramientas/", create_herramientas, name="create_herramientas"),
    path("muebles/listar_muebles/", listar_muebles, name="listar_muebles"),
    path("muebles/search_muebles/", search_muebles, name="search_muebles"),
    path("muebles/create_muebles/", create_muebles, name="create_muebles"),
    
]