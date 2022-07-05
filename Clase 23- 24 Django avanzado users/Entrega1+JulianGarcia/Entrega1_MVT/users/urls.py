
#URLS dentro de http://127.0.0.1:8000/productos/

from django.urls import path, include
from productos.views import Productos_all, Detail_product , Create_product ,Delete_product, Update_product, search_product,listar_herramientas,search_herramientas,create_herramientas,listar_muebles, search_muebles, create_muebles
from users.views import Detail_profile, Update_profile , Update_User, Detail_user,User_all,Edit_user_full , Edit_user_lite, Detail_user_lite
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path("listar_usuarios/", User_all.as_view(), name = "listar_usuarios"),
    path("detail_user/<int:pk>/", Detail_user.as_view(), name = "detail_user"),
    path("detail_user_lite/<int:pk>/", Detail_user_lite.as_view(), name = "detail_user_lite"),
    path("update_user/<int:pk>/", Update_User.as_view() , name= "update_user"),
    path("edit_user_full/<int:pk>/", Edit_user_full.as_view() , name= "edit_user_full"),
    path("edit_user_lite/<int:pk>/", Edit_user_lite.as_view() , name= "edit_user_lite"),
    path("password/", auth_views.PasswordChangeDoneView.as_view(), name = "password"),


    path("detail_profile/<int:pk>/", Detail_profile.as_view(), name = "detail_profile"), # aca con el <int:id> aclaramos que le vamos a pasar un entero llamado pk
    path("update_profile/<int:pk>/", Update_profile.as_view(), name = "update_profile"),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)