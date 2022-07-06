from dataclasses import fields
from msilib.schema import Class
import profile
from tkinter import Widget
from django import forms 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm    # importo el form de creae el user por defecto django para modificar
from django.contrib.auth.models import User             # importo el usuario por defecto de django
from users.models import User_profile




class User_change_form_lite(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}) )
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}) )
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}) )

    class Meta:
        model = User
        fields = ["username","email" , "first_name", "last_name"]
        help_texts = {k: "" for k in fields}                   # for re loco para que no muestre los help text 





#class Profile_change_form_lite(UserChangeForm):
    ##phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}) )
    #image = forms.ImageField()
    #user = forms.CharField()

    #class Meta:
        #model = User_profile
        #fields = ["phone","image"]
        #help_texts = {k: "" for k in fields}                   # for re loco para que no muestre los help text 
