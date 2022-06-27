from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class informacoesUsuario(models.Model):
    idade = models.CharField(max_length=3)
    GENEROS = [
        ('F', 'Feminino'),
        ('M', 'Masculino')
    ]
    genero = models.CharField(
        max_length=2,
        choices=GENEROS,
    )
    telefone = models.CharField(max_length=16)
    primeiroEmprego = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)