from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from usuarioApp.models import usuario

# Register your models here.
# class UsuarioInline(admin.StackedInline):
#     model = usuario
#     can_delete = False
#     verbose_name_plural = 'usuarios'

# class CustomizedUsuarioAdmin (UserAdmin):
#     inlines = (UsuarioInline, )

# admin.site.unregister(User)
# admin.site.register(User, CustomizedUsuarioAdmin)

# admin.site.register(usuario)