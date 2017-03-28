from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from cms.models import Pages

# Create your views here.
def base(request, recurso):
    try:
        pagina = Pages.objects.get(name=recurso)
        return HttpResponse(pagina.page)
    except Pages.DoesNotExist:
        return HttpResponseNotFound('La pagina no existe o ha introducido mal el recurso, introduzca [nombre]App')

def pepito(request):
    htmlAnswer = "<p> Pepito Saluda </p>"
    return HttpResponse(htmlAnswer)
