from django.urls import path

from . import views

app_name = 'calendario'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<str:fecha>/', views.calendario, name='fecha'),
]
