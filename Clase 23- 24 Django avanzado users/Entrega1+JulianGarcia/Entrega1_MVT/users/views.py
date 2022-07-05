from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView , CreateView, DeleteView , UpdateView
from django.urls import reverse
from users.models import User_profile  

# Create your views here.


#def profile(request):
    #user = request.user.user_profile.id
    #kwargs = {user}

    #return reverse('detail_user', kwargs)
    #return redirect('detail_user', kwargs = {'pk':user})



#class Profile(ListView):  
    #model = User_profile
    #template_name = "profile.html" 


    


class Detail_profile(DetailView):
    model = User_profile
    template_name = "detail_profile.html"
