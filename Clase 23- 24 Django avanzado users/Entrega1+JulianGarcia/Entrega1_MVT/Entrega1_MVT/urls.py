"""Entrega1_MVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Entrega1_MVT.views import index, contacto, login_view, logout_view, register_view, Update_User, Detail_user,User_all
from django.conf import settings # importo para lo de media 
from django.conf.urls.static import static # para imagenes 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index ,  name= "index" ),   # - Pagina de inicio
    path("productos/", include("productos.urls")), #- Subdirectorio Productos
    path("users/", include("users.urls")),
    path("contacto/", contacto , name= "contacto" ),
    path("login/", login_view , name= "login" ),
    path("logout/", logout_view , name= "logout" ),
    path("registrer/", register_view , name= "register" ),
    path("listar_usuarios/", User_all.as_view(), name = "listar_usuarios"),
    path("detail_user/<int:pk>/", Detail_user.as_view(), name = "detail_user"),
    path("update_user/<int:pk>/", Update_User.as_view() , name= "update_user"),

    

]




# para las imagenes 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)