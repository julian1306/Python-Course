from dataclasses import fields
from msilib.schema import Class
from tkinter import Widget
from django import forms 
from django.contrib.auth.forms import UserCreationForm     # importo el form de creae el user por defecto django para modificar
from django.contrib.auth.models import User              # importo el usuario por defecto de django


#form custom 

class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su Contraseña", widget=forms.PasswordInput)
    level = forms.IntegerField()

    class Meta:
        model = User
        fields = ["username","email" , "password1", "password2","level"]
        help_texts = {k: "" for k in fields}                   # for re loco para que no muestre los help text 


