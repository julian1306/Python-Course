from msilib.schema import Class
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.name
    


class Productos(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    new_price = models.IntegerField(null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)  # aca le digo que puede estan en blanco o nulo 
    SKU = models.CharField(max_length=30, unique=True) #unique=True) # --------- Aca le digo que el numero de identificacion tiene que ser unico 
    available = models.BooleanField(default=True) # ----------------- Aca le digo que por default esta disponible
    imagen = models.ImageField(upload_to="productos_imagenes", null=True)
    category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos',blank=True, null=True) # relacion con categorias entonces puedo hacer un categoria.productos
    class Meta:
        #abstract = True
        verbose_name= "producto"                      # nombre para el portal de admin en single el otro en plural
        verbose_name_plural = "productos"

    def __str__(self):                               # para que quede lindo 
        return self.name
    



class Productos_herramientas(Productos):
    energia = models.CharField(max_length=30,blank=True, null=True)
    clase = models.CharField(max_length=30,blank=True, null=True)


class Productos_muebles(Productos):
    tipo = models.CharField(max_length=30,blank=True, null=True)
    capacidad = models.CharField(max_length=30,blank=True, null=True)




class Muebles_exterior(Productos):
    resistencia = models.CharField(max_length=30,blank=True, null=True)









# CONTACTO 
class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)




