from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super(PublicadosManager, self).get_queryset().filter(estado='publicado')


class Publicacao(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    objects = models.Manager()
    publicados = PublicadosManager()

    titulo = models.CharField(max_length=250)
    subtitulo = models.SlugField(max_length=250, unique_for_date='data_publicacao')
    descricao = models.CharField(max_length=250, unique_for_date='data_publicacao')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogc_publicacoes')
    corpo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')

    class Meta:
        ordering = ('-data_publicacao',)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blogc:details', args=[self.subtitulo])
