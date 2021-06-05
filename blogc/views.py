from django.shortcuts import render
from blogc.models import Publicacao


# Create your views here.
def index(request):
    return render(request, 'index.html', {'user': request.user})


def posts(request):
    publicacoes = Publicacao.publicados.all()
    return render(request, 'publicacao/lista.html', {'posts': publicacoes, 'user': request.user})


def details(request, _subtitulo):
    publicacao = get_object_or_404(Publicacao, subtitulo=_subtitulo, estado='publicado')
    return render(request,
                  'publicacao/detalhe.html',
                  {'post': publicacao, 'user': request.user})
