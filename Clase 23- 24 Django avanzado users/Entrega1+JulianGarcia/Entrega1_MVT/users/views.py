from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView , CreateView, DeleteView , UpdateView
from django.urls import reverse
from users.models import User_profile  

# Create your views here.



class Detail_profile(DetailView):
    model = User_profile
    template_name = "detail_profile.html"





class Update_profile(UpdateView):
    model = User_profile
    template_name = 'update_profile.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_profile', kwargs = {'pk':self.object.pk}) 