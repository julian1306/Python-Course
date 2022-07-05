from dataclasses import fields
from msilib.schema import Class
from tkinter import Widget
from django import forms 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm    # importo el form de creae el user por defecto django para modificar
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



class User_change_form(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}) )
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}) )
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}) )

    class Meta:
        model = User
        fields = ["username","email" , "first_name", "last_name"]
        help_texts = {k: "" for k in fields}                   # for re loco para que no muestre los help text 

