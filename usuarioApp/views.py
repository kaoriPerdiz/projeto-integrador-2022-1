from django.shortcuts import render, redirect
from .models import usuario
from django.views.decorators.http import require_POST
from dicaApp import urls
from django.contrib.auth.models import User

def cadastro(request):
    return render(request, 'cadastro.html')

@require_POST
def cadastrar(request):
    if request.method=='POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        print(nome)
        novoUsuario = User.objects.create_user(username=nome, email=email, password=senha)
        novoUsuario.save()
        return render(request, 'dicas/todasDicas.html')

def login(request):
    return render(request, 'login.html')