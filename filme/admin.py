from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# só existe para criar o campo personalizado no admin do site
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico de vídeos",{'fields':('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)
# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)