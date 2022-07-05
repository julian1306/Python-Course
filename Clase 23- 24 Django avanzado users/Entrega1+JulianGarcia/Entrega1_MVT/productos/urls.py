
#URLS dentro de http://127.0.0.1:8000/productos/

from django.urls import path, include
from productos.views import Productos_all, Detail_product , Create_product ,Delete_product, Update_product, search_product,listar_herramientas,search_herramientas,create_herramientas,listar_muebles, search_muebles, create_muebles
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    
    path("listar_productos/", Productos_all.as_view() , name ="listar_productos"),# hay que aclarar que la clase va como una lista con as view 
    path("crear_productos/", Create_product.as_view(), name="crear_productos"),
    path("product_detail/<int:pk>/", Detail_product.as_view(), name = "detail_product"), # aca con el <int:id> aclaramos que le vamos a pasar un entero llamado pk
    path("delete_product/<int:pk>/", Delete_product.as_view(), name = "delete_product"),   # Aca creo las urls de products y llamo a las views de product
    path('update_product/<int:pk>/', Update_product.as_view(), name = 'update_product'),
    path("buscar_productos/", search_product, name = "buscar_productos"),
    path("herramientas/listar_herramientas/", listar_herramientas, name="listar_herramientas"),
    path("herramientas/search_herramientas/", search_herramientas, name="search_herramientas"),
    path("herramientas/create_herramientas/", create_herramientas, name="create_herramientas"),
    path("muebles/listar_muebles/", listar_muebles, name="listar_muebles"),
    path("muebles/search_muebles/", search_muebles, name="search_muebles"),
    path("muebles/create_muebles/", create_muebles, name="create_muebles"),

    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)