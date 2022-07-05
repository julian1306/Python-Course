
#URLS dentro de http://127.0.0.1:8000/productos/

from django.urls import path, include
from productos.views import Productos_all, Detail_product , Create_product ,Delete_product, Update_product, search_product,listar_herramientas,search_herramientas,create_herramientas,listar_muebles, search_muebles, create_muebles
from users.views import Detail_profile, Update_profile
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    
    path("detail_profile/<int:pk>/", Detail_profile.as_view(), name = "detail_profile"), # aca con el <int:id> aclaramos que le vamos a pasar un entero llamado pk
    path("update_profile/<int:pk>/", Update_profile.as_view(), name = "update_profile"),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)