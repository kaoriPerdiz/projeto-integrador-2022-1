from django.contrib import admin
from dicaApp.models import dica
from tagApp.models import tag
from usuarioApp.models import usuario
# Register your models here.
admin.site.register(dica)
admin.site.register(usuario)
admin.site.register(tag)