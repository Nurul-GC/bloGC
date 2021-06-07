from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogc.models import Publicacao


# Create your views here.
def index(request):
    return render(request, 'index.html', {'user': request.user})


def publicados(request):
    lista_publicacoes = Publicacao.publicados.all()
    paginator = Paginator(lista_publicacoes, 3)  # 5 publicados in each page
    pagina = request.GET.get('page')
    try:
        publicacoes = paginator.page(pagina)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        publicacoes = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        publicacoes = paginator.page(paginator.num_pages)
    return render(request, 'publicacao/lista.html', {'page': pagina, 'posts': publicacoes, 'user': request.user})


def rascunhos(request):
    lista_publicacoes = Publicacao.rascunhos.all()
    paginator = Paginator(lista_publicacoes, 3)  # 5 publicados in each page
    pagina = request.GET.get('page')
    try:
        publicacoes = paginator.page(pagina)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        publicacoes = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        publicacoes = paginator.page(paginator.num_pages)
    return render(request, 'publicacao/lista.html', {'page': pagina, 'posts': publicacoes, 'user': request.user})


def detalhes(request, _subtitulo):
    publicacao = get_object_or_404(Publicacao, subtitulo=_subtitulo, estado='publicado')
    return render(request,
                  'publicacao/detalhe.html',
                  {'post': publicacao, 'user': request.user})
