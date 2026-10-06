from django.shortcuts import render

def homepage(request):
    """Render the project homepage."""
    return render(request, 'home.html')