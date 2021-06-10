from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blogc.forms import ComentarioForm, PublicacaoForm
from blogc.models import Publicacao


# Create your views here.
@login_required()
def index(request):
    nova_publicacao = None
    if request.method == 'POST':
        formulario_publicacao = PublicacaoForm(data=request.POST)
        if formulario_publicacao.is_valid():
            nova_publicacao = formulario_publicacao.save()
    else:
        formulario_publicacao = PublicacaoForm()
    return render(request, 'index.html',
                  {'user': request.user,
                   'postform': formulario_publicacao,
                   'new_post': nova_publicacao})


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


@login_required()
def detalhes(request, _subtitulo):
    publicacao = get_object_or_404(Publicacao, subtitulo=_subtitulo, estado='publicado')
    comentario = publicacao.comentarios.filter(ativo=True)
    novo_comentario = None
    if request.method == 'POST':
        formulario_comentario = ComentarioForm(data=request.POST)
        if formulario_comentario.is_valid():
            novo_comentario = formulario_comentario.save(commit=False)
            novo_comentario.post = publicacao
            novo_comentario.save()
    else:
        formulario_comentario = ComentarioForm()
    return render(request, 'publicacao/detalhe.html',
                  {'post': publicacao, 'user': request.user,
                   'comments': comentario, 'new_comment': novo_comentario,
                   'commentform': formulario_comentario})
