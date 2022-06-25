from django.db import models

# Create your models here.
class dica(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    autor = models.ForeignKey('usuarioApp.usuario', on_delete=models.CASCADE)
    tag = models.ForeignKey('tagApp.tag', on_delete=models.CASCADE)
    criacao = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, default=titulo)

    class Meta:
        ordering = ("-criacao",)

    def __str__(self):
        return self.titulo