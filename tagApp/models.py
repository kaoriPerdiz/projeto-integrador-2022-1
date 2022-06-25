from django.db import models

# Create your models here.
class tag(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo