from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro')
]
