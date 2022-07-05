from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.urls import reverse
from users.models import User_profile  
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin  # para req de logeado
from django.views.generic import View, ListView, DetailView , CreateView, DeleteView , UpdateView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

# Create your views here.


# !!!!!!!!!!!!!!!!!!!!!!! USERS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 



## permisos custom # 

class SecureView(PermissionRequiredMixin):
    ...
    permission_required = 'auth.view_user'             # para varios ( 'auth.change_user'  , "otro permiso")
    ...


    # 'auth.change_user'



class User_all(SecureView,ListView):                 # reemplazar (PermissionRequiredMixin, Listview)
    #permission_required = 'auth.change_user'              # se puede poner aca para poniendo directo el PermissionRequiredMixin de django u abajo el permission_required que uno quiera 
    model = User
    template_name = "listar_usuarios.html" 



class Detail_user(LoginRequiredMixin,DetailView):
    model= User
    template_name = "detail_user.html"



class Update_User(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'update_user.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_user', kwargs = {'pk':self.object.pk}) # lo mando al url dle name detail_product con el id


# Con from class para modificar mejor 

class Edit_user(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'edit_user.html'


    #def get_object(self):                                 # funcion para sacar el user en class 
    #    return self.request.user


    def get_success_url(self):
        return reverse('detail_user', kwargs = {'pk':self.object.pk}) 







# !!!!!!!!!!!!!!!!!!!!!!! PROFILE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 

class Detail_profile(DetailView):
    model = User_profile
    template_name = "detail_profile.html"



class Update_profile(UpdateView):
    model = User_profile
    template_name = 'update_profile.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_profile', kwargs = {'pk':self.object.pk}) 