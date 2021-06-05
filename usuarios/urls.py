from django.urls import path, include
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('cadastro/', views.cadastro, name='cadastro')
]
