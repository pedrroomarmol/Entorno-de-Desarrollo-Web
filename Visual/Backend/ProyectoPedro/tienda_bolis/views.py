from django.shortcuts import render

def home(request):
    return render(request, 'tienda_bolis/home.html')


def contact(request):
    return render(request, 'tienda_bolis/contact.html')
