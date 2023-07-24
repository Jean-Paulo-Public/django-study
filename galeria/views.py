from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    dados = {
             1:{"title": "Python",
                "text": "Python é uma linguagem de programação"},
             2:{"title": "DJango",
                "text": "Django e um framework python"}                
            }
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')