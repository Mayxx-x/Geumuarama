import os
from pathlib import Path
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
    gallery_index = {}
    image_path = Path(__file__).resolve().parent.parent.joinpath('static/gallery/')

    for image in image_path.iterdir():
        #generate a dict with key being directory name and value being list of images name only
        if image.is_dir():
            gallery_index[image.name] = [img.name for img in image.iterdir()]

    context = {
        'active': 'photos',
        'gallery_index': gallery_index
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