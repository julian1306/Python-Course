"""A_proyecto_Clase_19_root URL Configuration

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
from A_proyecto_Clase_19_root.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name= "index" ),   # ------------------- Pagina de inicio que de una te mande aca al template de index que cree 
    path("productos/", include("productos.urls")),   #con esto creamos un subdirectorio productos/ y que busque las otras url ahi adentro de la app. es decir ne productos.urls.py 
]
