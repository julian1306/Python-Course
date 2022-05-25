from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def saludo(request):
    return







def return_template(request):
    context = {

    }


    return render(request, 'template_1.html', context = context)
