from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        "contatos": contatos
    })
