from django.shortcuts import get_object_or_404, redirect, render

from .forms import ComentarioForm, ReceitasForm
from .models import Comentario, Receitas


def home(request):
    most= Receitas.objects.all()
    return render(request, 'comida/site mrreceitas.html',{'most': most})


def buchada(request):
    return render(request, 'comida/pagina de buchada.html')


def inhoque(request):
    return render(request, 'comida/pagina de inhoque.html')

def bolo(request):
    return render(request, 'comida/pagina do bolo.html')

def formulario(request):
    form = ReceitasForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ReceitasForm()
        return render(request, 'comida/formulario.html', {'form': form})
    
def mostr(request, id):
    amostrar = get_object_or_404(Receitas, pk=id)
    return render(request, 'comida/mostr.html', {'amostrar': amostrar})

def comentarios(request):
    com= Comentario.objects.all()
    return render(request, 'comida/comentario.html',{'com': com})

def comentar(request):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = ComentarioForm()
        return render(request, 'comida/comentar.html', {'form': form})
    
def sobre(request):
    return render(request, 'comida/sobre.html')