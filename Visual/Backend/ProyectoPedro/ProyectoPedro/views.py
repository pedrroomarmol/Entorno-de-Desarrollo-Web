from django.shortcuts import render


def homepage(request):
    request.session.set_expiry(2 * 60 * 60)
    visitas = request.session.get("visitas_home", 0)
    visitas += 1
    request.session["visitas_home"] = visitas
    return render(request, "home.html", {
        "visitas" : visitas
    })