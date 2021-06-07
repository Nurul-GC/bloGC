from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogc.models import Publicacao
from blogc.forms import PartilharPublicacaoForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {'user': request.user})


def posts(request):
    lista_publicacoes = Publicacao.publicados.all()
    paginator = Paginator(lista_publicacoes, 5)  # 5 posts in each page
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


def details(request, _subtitulo):
    publicacao = get_object_or_404(Publicacao, subtitulo=_subtitulo, estado='publicado')
    return render(request,
                  'publicacao/detalhe.html',
                  {'post': publicacao, 'user': request.user})


def share(request, post_id):
    post = get_object_or_404(Publicacao, id=post_id, estado='publicado')
    enviar = False
    if request.method == 'POST':
        form = PartilharPublicacaoForm()
        if form.is_valid():
            dados_validos = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{dados_validos['nome']} recomendou que lê-ses {post.titulo}"
            message = f"Leia {post.titulo} em {post_url}\n\n" \
                      f"Comentario de '{dados_validos['nome']}': {dados_validos['comentario']}"
            send_mail(subject, message, 'admin@myblog.com', [dados_validos['destinatario']])
            enviar = True
    else:
        form = PartilharPublicacaoForm()
    return render(request, 'publicacao/partilhar.html', {'post': post, 'form': form, 'sent': enviar})
