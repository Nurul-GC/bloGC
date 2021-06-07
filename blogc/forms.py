from django import forms


class PartilharPublicacaoForm(forms.Form):
    nome = forms.CharField(max_length=25)
    email = forms.EmailField()
    destinatario = forms.EmailField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)
