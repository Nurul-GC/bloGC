from django.urls import path
from blogc import views

app_name = 'blogc'
urlpatterns = [
    path('', views.index, name='index'),
    path('publicados/', views.publicados, name='publicados'),
    path('rascunhos/', views.rascunhos, name='rascunhos'),
    path('<slug:_subtitulo>/', views.detalhes, name='detalhes'),
    path('tag/<slug:tag_subtitulo>/',  views.publicados, name='tags'),
    path('editar/<slug:_subtitulo>/', views.editar, name='editar')
]
