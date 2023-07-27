from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):

    return render(request, "index.html")

def content(request):
    return render(request, "_content.html")

def contato(request):
    return render(request, "_contact.html")