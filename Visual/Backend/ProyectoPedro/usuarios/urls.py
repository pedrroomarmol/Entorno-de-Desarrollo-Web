from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("iniciar-sesion/", views.iniciar_sesion, name="iniciar_sesion"),
    path(
        "cerrar-sesion/",
        LogoutView.as_view(next_page="usuarios:iniciar_sesion"),
        name="cerrar_sesion",
    ),
]