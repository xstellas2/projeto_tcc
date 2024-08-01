from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path("", index)
    path("", agrotoxico)
    path("", base)
    path("", deletar_sugestao)
    path("", editar_sugestoes)
    path("", formulario)
    path("", gafanhotos)
    path("", index)
    path("", lagartas)
    path("", listagem_sugestoes)
    path("", sobre_nos)
]