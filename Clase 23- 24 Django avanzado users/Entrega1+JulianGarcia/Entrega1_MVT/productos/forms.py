from dataclasses import fields
from msilib.schema import Class
from django import forms   #Aca importo los formularios de django 
from productos.models import Productos, Productos_herramientas, Productos_muebles, Contacto  # Aca importo el modelo Productos para usarlo  caundo creo la cass form 



#Create your Forms here 


class Product_form(forms.ModelForm):                   # Aca lo creo pero de manera mas rapida llamando a los Modelform
    class Meta:
        model = Productos
        fields = '__all__'



class Herramientas_form(forms.ModelForm):
    class Meta:
        model = Productos_herramientas
        fields = '__all__'    



class Muebles_form(forms.ModelForm):
    class Meta:
        model = Productos_muebles
        fields = '__all__'


class Contacto_form(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
