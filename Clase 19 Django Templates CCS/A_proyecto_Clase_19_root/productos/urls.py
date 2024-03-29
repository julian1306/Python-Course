
#URLS dentro de http://127.0.0.1:8000/productos/

from django.urls import path, include
from productos.views import productos_all,create_product, search_product, detail_product    # importo las def de views para laburar las URL 




urlpatterns = [
    
    path("listar_productos/", productos_all , name = "listar_productos"),
    path("crear_productos/", create_product, name="crear_productos"),  # Aca creo las urls de products y llamo a las views de product 
    path("buscar_productos/", search_product, name = "buscar_productos"),
    path("product_detail/<int:pk>/", detail_product, name = "product_detail"), # aca con el <int:id> aclaramos que le vamos a pasar un entero llamado pk 
    
]



