from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Pagina Inicial"),
    path("/escotismo", views.content, name="content")
]