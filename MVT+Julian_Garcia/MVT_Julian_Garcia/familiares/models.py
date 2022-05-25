from django.db import models



# Create your models here.


class Familiares(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.FloatField(max_length=200, blank=True, null=True)
    dni = models.FloatField(max_length=8)
    fecha_nacimiento = models.CharField(max_length=100,blank=True, null=True)
    

