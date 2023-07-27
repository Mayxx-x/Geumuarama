from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "index.html")

def escotismo(request):
    return render(request, "_content/_escotismo.html")

def about(request):
    return render(request, "_content/_about.html")

def roles(request):
    return render(request, "_content/_roles.html")

def photos(request):
    return render(request, "_content/_fotos.html")

def infos(request):
    return render(request, "_content/_infos.html")

def downloads(request):
    return render(request, "_content/_downloads.html")

def contato(request):
    return render(request, "_content/_contact.html")