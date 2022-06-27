from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from dicaApp import views as dicaView

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('loginAndamento/', views.loginAndamento, name='loginAndamento'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('cadastrarInformacoes/', views.cadastrarInformacoes, name='cadastrarInformacoes'),
    path('cadastroSucesso/', dicaView.todas_dicas, name='cadastroSucesso')
]