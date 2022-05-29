
#URLS dentro de http://127.0.0.1:8000/productos/

from django.urls import path, include
from productos.views import producto, productos_all    # importo las def de views para laburar las URL 



urlpatterns = [
    path("crear_producto_nuevo/", producto, name="crear produto nuevo"),
    path("listar_productos/", productos_all , name = "listar productos"),
    
]



