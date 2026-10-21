from django.urls import path
from . import views

app_name = 'tienda_bolis'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contact, name='contact'),
]