from django.shortcuts import render, redirect
from .models import dica
from tagApp.models import tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
import requests

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

def sair(request):
    logout(request)
    return redirect('/usuario/login')

def enquete(request):
    return render(request, 'enquete.html', {'tags': tags})

@require_POST
def votar(request):
    if request.method == "POST":
        motivo = request.POST['motivo']
        requests.post('https://enquete-entrevista-default-rtdb.firebaseio.com/motivoentrevista.json', json = {'motivo':motivo})
        resposta = requests.get('https://enquete-entrevista-default-rtdb.firebaseio.com/motivoentrevista.json')

        motivo1 = 0
        motivo2 = 0
        motivo3 = 0
        total = 0

        for value in resposta.json().items():
            if value[1]['motivo'] == '1':
                motivo1+=1
                
            elif value[1]['motivo'] == '2':
                motivo2+=1
                
            elif value[1]['motivo'] == '3':
                motivo3+=1
            
        total = motivo1+motivo2+motivo3
        motivo1 = round(100*motivo1/total, 1)
        motivo2 = round(100*motivo2/total, 1)
        motivo3 = round(100*motivo3/total, 1)
        return render(request, 'enqueteResultado.html', {'motivoEscolhido': motivo, 'motivo1': motivo1,'motivo2': motivo2,'motivo3': motivo3})
    