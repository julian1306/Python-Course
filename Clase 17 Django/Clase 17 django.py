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


# Crear usuario admin 

# PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\Clase 17 Django\proyecto_x2> python manage.py createsuperuser 


# crear apps con startapp 

#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia> cd .\MVT_Julian_Garcia\
#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia\MVT_Julian_Garcia> python manage.py startapp familiares



#Cuando hacer cambios en la DB o en los modelos 

#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia\MVT_Julian_Garcia> python manage.py makemigrations
#No changes detected
#PS C:\Users\Julian\Documents\GitHub\Julian-Python-Curso\MVT+Julian_Garcia\MVT_Julian_Garcia> python manage.py migrate  