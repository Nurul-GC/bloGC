from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super(PublicadosManager, self).get_queryset().filter(estado='publicado')


class RascunhosManager(models.Manager):
    def get_queryset(self):
        return super(RascunhosManager, self).get_queryset().filter(estado='rascunho')


class Publicacao(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    objects = models.Manager()
    publicados = PublicadosManager()
    rascunhos = RascunhosManager()

    titulo = models.CharField(max_length=250)
    subtitulo = models.SlugField(max_length=250, unique_for_date='data_publicacao',
                                 help_text='<b style="color:black;">O subtitulo deve ser igual ao titulo, mas transcrito em minusculas e com espacos substituidos por (-)(hifens).'
                                           '<br>Ex: nome-para-a-publicacao.</b>')
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
        return reverse('blogc:detalhes', args=[self.subtitulo])


class Comentario(models.Model):
    post = models.ForeignKey(Publicacao, on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    corpo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ('criado',)

    def __str__(self):
        return f'Comentario de {self.nome} para {self.post}.'
