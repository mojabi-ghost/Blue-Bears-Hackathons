from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def login(request):
    template = loader.get_template('UnilinkedApp/index.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('UnilinkedApp/register.html')
    return HttpResponse(template.render())