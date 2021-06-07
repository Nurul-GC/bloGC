from django.urls import path
from blogc import views

app_name = 'blogc'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:_subtitulo>/', views.details, name='details'),
    path('post/share/<int:post_id>/', views.share, name='share')
]
