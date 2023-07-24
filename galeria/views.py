from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    dados = {
             1:{"title": "Python",
                "text": "Python é uma linguagem de programação",
                "foto": "/assets/imagens/Python_Logo.webp"},
             2:{"title": "DJango",
                "text": "Django e um framework python",
                "foto": "/assets/imagens/Django-Framework-Logo.png"}                
            }
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')