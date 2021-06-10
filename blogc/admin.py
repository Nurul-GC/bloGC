from django.contrib import admin
from blogc.models import Publicacao, Comentario


# Register your models here.
@admin.register(Publicacao)
class PulicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'autor', 'data_publicacao', 'estado')
    list_filter = ('estado', 'data_criacao', 'data_publicacao', 'autor')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'subtitulo': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'data_publicacao'
    ordering = ('estado', 'data_publicacao')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'post', 'criado', 'ativo')
    list_filter = ('ativo', 'criado', 'atualizado')
    search_fields = ('nome', 'email', 'corpo')
