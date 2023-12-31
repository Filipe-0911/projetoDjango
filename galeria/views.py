from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'index.html', {"cards" : fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] #referencia ao name buscar do input
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains = nome_a_buscar)
            
    return render(request, "buscar.html", {"cards" : fotografias})