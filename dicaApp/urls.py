from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.todas_dicas, name='todas_dicas'),
    path('detalhe/<int:pk>', views.detalhe_dica, name='detalhe_dica'),
    path('categoria/<int:pk>', views.filtrar_tag, name='filtrar_tag')
]