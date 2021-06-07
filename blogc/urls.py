from django.urls import path
from blogc import views

app_name = 'blogc'
urlpatterns = [
    path('', views.index, name='index'),
    path('publicados/', views.publicados, name='publicados'),
    path('rascunhos/', views.rascunhos, name='rascunhos'),
    path('publicacao/<slug:_subtitulo>/', views.detalhes, name='detalhes'),
]
