from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.urls import reverse, reverse_lazy
from users.models import User_profile  
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin  # para req de logeado
from django.views.generic import View, ListView, DetailView , CreateView, DeleteView , UpdateView
from users.forms import User_change_form_lite 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

# Create your views here.


# !!!!!!!!!!!!!!!!!!!!!!! USERS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 



## permisos custom # 

class SecureView_user(PermissionRequiredMixin):
    ...
    permission_required = ('auth.add_user','auth.change_user','auth.delete_user','auth.view_user')           # para varios ( 'auth.change_user'  , "otro permiso")
    ...
    # Brian tiene esos permisos asi que pasa .


    # 'auth.change_user'



class User_all(SecureView_user,ListView):                 # reemplazar (PermissionRequiredMixin, Listview)
    #permission_required = 'auth.change_user'              # se puede poner aca para poniendo directo el PermissionRequiredMixin de django u abajo el permission_required que uno quiera 
    model = User
    template_name = "listar_usuarios.html" 



class Detail_user(LoginRequiredMixin,DetailView):
    model= User
    template_name = "detail_user.html"


## YA NO NECESARIO OLD 
#class Update_User(LoginRequiredMixin,UpdateView):
    #model = User
    ##template_name = 'update_user.html'
    #fields = '__all__'

#
    ##def get_success_url(self):
        #return reverse('detail_user', kwargs = {'pk':self.object.pk}) # lo mando al url dle name detail_product con el id


# Con from class para modificar mejor 
# Especifico para el listar usuarios de los admin / staff 
class Edit_user_full(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'edit_user_full.html'


    #def get_object(self):                                 # funcion para sacar el request user en class en este caso no conviene 
    #    return self.request.user


    def get_success_url(self):
        return reverse('detail_user', kwargs = {'pk':self.object.pk}) 


#!!!!!!!!!!!!!!!!!!!!!!! PASSWORD!!!!!!!!!!!!!!!!!!!! 

class Custom_password_change_view(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("index")














# !!!!!!!!!!!!!!!!!!!!!! EDIT USER LITE !!!!!!!!!!!!!!!!!!!!!!!!! 

# lite para el boton de 

class Detail_user_lite(LoginRequiredMixin,DetailView):
    model= User
    template_name = "detail_user_lite.html"

    def get_object(self):                                 # funcion para sacar el request user en class 
        return self.request.user


class Edit_user_lite(LoginRequiredMixin,UpdateView):
    #model = User
    form_class = User_change_form_lite
    template_name = 'edit_user_lite.html'


    def get_object(self):                                 # funcion para sacar el request user en class 
        return self.request.user


    def get_success_url(self):
        return reverse('detail_user_lite', kwargs = {'pk':self.object.pk}) 

class Delete_user(LoginRequiredMixin,DeleteView):        
    model = User
    template_name = "delete_user.html"

    def get_success_url(self):
        return reverse("index") # Elimina y nos manda a index 




# !!!!!!!!!!!!!!!!!!!!!!! PROFILE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 


class Create_profile(LoginRequiredMixin,CreateView):
    def get_object(self):                                  # funcion para sacar el request user en class 
        return self.request.user
    
    model = User_profile
    user = get_object
    template_name = "create_profile.html"
    fields = "__all__"


    def get_success_url(self):
        return reverse('detail_profile',kwargs={'pk':self.object.pk} )




class Detail_profile(LoginRequiredMixin,DetailView):
    model = User_profile
    template_name = "detail_profile.html"



class Update_profile(LoginRequiredMixin,UpdateView):
    model = User_profile
    template_name = 'update_profile.html'
    fields = ["phone","image"]


    def get_success_url(self):
        return reverse('detail_profile', kwargs = {'pk':self.object.pk}) 



class Delete_profile(LoginRequiredMixin,DeleteView):        
    model = User_profile
    template_name = "delete_profile.html"

    def get_success_url(self):
        return reverse("index") # Elimina y nos manda a index 
