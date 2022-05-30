from msilib.schema import Class
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.


class Productos(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=5000, blank=True, null=True)  # aca le digo que puede estan en blanco o nulo 
    SKU = models.CharField(max_length=30) #unique=True) # --------- Aca le digo que el numero de identificacion tiene que ser unico 
    available = models.BooleanField(default=True) # ----------------- Aca le digo que por default esta disponible . 
    class Meta:
        verbose_name= "producto"                      # nombre para el portal de admin en single el otro en plural
        verbose_name_plural = "productos"


