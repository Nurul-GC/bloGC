from django.db.models import Count

from blogc.models import Publicacao


def total_posts():
    return len(Publicacao.publicados.all())


def get_most_commented_posts(count=5):
    mais_comentarios = Publicacao.publicados.annotate(
        total_comentarios=Count('comentarios')).order_by('-total_comentarios')[:count]
    return mais_comentarios


def show_latest_posts(count=5):
    publicacoes_recentes = Publicacao.publicados.order_by('-data_publicacao')[:count]
    return publicacoes_recentes
