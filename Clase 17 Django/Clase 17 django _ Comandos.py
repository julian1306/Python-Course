#instalacion Django .

# Correr el terminal desde la carpeta don de estemos marados en este c aso la de Clase 17 Django
#- PS G:\Mi unidad\Curso Python Files\Clase 17 Django> pip install django
#-PS G:\Mi unidad\Curso Python Files\Clase 17 Django> django-admin startproject proyecto_x
#-PS G:\Mi unidad\Curso Python Files\Clase 17 Django> cd .\proyecto_x\
#-PS G:\Mi unidad\Curso Python Files\Clase 17 Django\proyecto_x> 

#con este crea el server local en http://127.0.0.1:8000/ o local host

# - PS G:\Mi unidad\Curso Python Files\Clase 17 Django\proyecto_xx> python manage.py runserver

#admin por default
#-http://127.0.0.1:8000/admin/login/?next=/admin/


#import importante para el views del root : 

from django.http import HttpRequest
from django.shortcuts import render  


# Crear usuario admin 

# PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\Clase 17 Django\proyecto_x2> python manage.py createsuperuser 


# crear apps con startapp 

#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia> cd .\MVT_Julian_Garcia\
#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia\MVT_Julian_Garcia> python manage.py startapp familiares


# COMO REGISTRAR LAS APP EN EL SITE ADMIN 
# en el admin.py de la app registrar asi con su correspondiente import antes 

# admin.site.register(Familiares)



# Como configurar el path de templates en el proyecto 

#En las setting del projecto root cambiar :_ 

#TEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'DIRS': [BASE_DIR/'templates'], ------------------------CAMBIAR ACA PONER SIEMPRE BASE_DIR/'templates' y crear una carpeta que sellame tempaltes 



#Cuando hacer cambios en la DB o en los modelos 

#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia\MVT_Julian_Garcia> python manage.py makemigrations
#No changes detected
#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia\MVT_Julian_Garcia> python manage.py migrate  



#requerimientos 

#pip freeze 
#pip freeze > requirements.txt