from django.contrib import admin

from .models import Comentario, Receitas

admin.site.register(Receitas)
admin.site.register(Comentario)