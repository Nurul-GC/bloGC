from django import forms

from blogc.models import Comentario, Publicacao


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nome', 'email', 'corpo')
        widgets = {'corpo': forms.Textarea({'col': 50, 'placeholder': 'Escreva aqui o seu comentario'}),
                   'nome': forms.TextInput({'placeholder': 'Digite o seu nome'}),
                   'email': forms.EmailInput({'placeholder': 'Digite o seu email'})}


class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ('titulo', 'subtitulo', 'descricao', 'autor', 'corpo', 'estado')
        labels = {'estado': 'Defina o estado da sua publicacao:',
                  'autor': 'Selecione o autor para a publicacao:'}
        prepopulated_fields = {'subtitulo': 'titulo'}
        widgets = {'titulo': forms.TextInput({'placeholder': 'Digite um titulo para a sua publicacao'}),
                   'subtitulo': forms.TextInput({'placeholder': 'Digite o subtitulo para a sua publicacao'}),
                   'descricao': forms.TextInput({'placeholder': 'Descreva a sua publicacao'}),
                   'corpo': forms.Textarea({'col': 50, 'placeholder': 'Escreva aqui o conteudo da sua publicacao'})}
