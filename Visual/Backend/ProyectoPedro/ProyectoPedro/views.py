from django.shortcuts import render

def homepage(request):
    """Render the applications portal."""
    return render(request, 'home.html')