from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "_content/_home.html")

def faq(request):
    return render(request, "_content/_faq.html")

def escotismo(request):
    context = {
        'active': 'escotismo'
    }
    return render(request, "_content/_escotismo.html", context)

def about(request):
    context = {
        'active': 'about'
    }
    return render(request, "_content/_about.html", context)

def roles(request):
    context = {
        'active': 'roles'
    }
    return render(request, "_content/_roles.html", context)

def photos(request):
    context = {
        'active': 'photos'
    }
    return render(request, "_content/_fotos.html", context)

def infos(request):
    context = {
        'active': 'infos'
    }
    return render(request, "_content/_infos.html", context)

def downloads(request):
    context = {
        'active': 'downloads'
    }
    return render(request, "_content/_downloads.html", context)

def contato(request):
    context = {
        'active': 'contato'
    }
    return render(request, "_content/_contact.html", context)