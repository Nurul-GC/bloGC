from django.urls import path
from blogc import views

app_name = 'blogc'
urlpatterns = [
    path('', views.index, name='index')
]
