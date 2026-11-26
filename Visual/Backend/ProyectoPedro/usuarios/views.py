from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_not_required
from .forms import RegistroForm


@login_not_required
def registro(request):
    form = RegistroForm(
        request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("usuarios:iniciar_sesion")
    return render(request, "usuarios/registro.html", {"form": form})

@login_not_required
def iniciar_sesion(request):
    form = AuthenticationForm(
        request,
        data=request.POST if request.method == "POST" else None
    )
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("/")
    return render(request, "usuarios/iniciar_sesion.html", {"form": form})


