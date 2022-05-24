from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Buenas Tardes gente Bella ")