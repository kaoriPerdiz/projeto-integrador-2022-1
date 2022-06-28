from django.shortcuts import render, redirect
from .models import informacoesUsuario
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/dicas')
    return render(request, "cadastro.html")


def informacoes(request):
    if request.user.is_authenticated:
        return redirect('/dicas')
    return render(request, "informacoes.html")


@require_POST
def cadastrarInformacoes(request):
    if request.method == "POST":
        idade = request.POST["idade"]
        genero = request.POST["genero"]
        telefone = request.POST["telefone"]
        primeiroEmprego = True if request.POST["primeiroEmprego"] == 'sim' else False
        usuario = request.POST["usuario"]
        usuarioInserido = User.objects.get(username = usuario)
        informacoesUsuarioNovo = informacoesUsuario(
            idade=idade,
            genero=genero,
            telefone=telefone,
            primeiroEmprego=primeiroEmprego,
            usuario=usuarioInserido
        )
        informacoesUsuarioNovo.save()
        return redirect('/dicas')


@require_POST
def cadastrar(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["senha"]
        novoUsuario = User.objects.create_user(
            username=email, email=email, password=senha, first_name=nome
        )
        novoUsuario.save()
        return render(request, "informacoes.html", {"novoUsuario": novoUsuario})


def login(request):
    if request.user.is_authenticated:
        return redirect('/dicas')
    return render(request, "login.html")

@require_POST
def loginAndamento(request):
    email = request.POST['email']
    senha = request.POST['senha']
    user = authenticate(request, username=email, password=senha)
    if user is not None:
        auth_login(request, user)
        return redirect('/dicas')
    else:
        return render(request, "login.html")