from django.shortcuts import render
from .models import dica
from tagApp.models import tag
from django.contrib.auth.decorators import login_required

tags = tag.objects.all()
# Create your views here.
@login_required(login_url='/usuario/login/')
def todas_dicas(request):
    dicas = dica.objects.all()
    return render(request, 'todasDicas.html', {'dicas': dicas, 'tags': tags})

@login_required(login_url='/usuario/login/')
def detalhe_dica(request, pk):
    dica_selecionada = dica.objects.get(id = pk)
    return render(request, 'detalheDica.html', {'dica_selecionada': dica_selecionada, 'tags': tags})

@login_required(login_url='/usuario/login/')
def filtrar_tag(request, pk):
    dicas_filtradas = dica.objects.filter(tag__id = pk)
    return render(request, 'porCategoria.html', {'dicas_filtradas': dicas_filtradas, 'tags': tags})