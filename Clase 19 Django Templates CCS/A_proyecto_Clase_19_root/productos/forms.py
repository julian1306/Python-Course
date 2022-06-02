from django import forms   #Aca importo los formularios de django 
from productos.models import Productos  # aca importo el modelo Productos para usarlo  caundo creo la cass form 


# class Product_form(forms.Form):             # Aca creo el formulario a mano 
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     available = forms.BooleanField()

class Product_form(forms.ModelForm):                   # Aca lo creo pero de manera mas rapida llamando a los Modelform
    class Meta:
        model = Productos
        fields = '__all__'
