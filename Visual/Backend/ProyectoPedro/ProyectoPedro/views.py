from django.shortcuts import render

def homepage(request):
    """Render the pen shop as the project homepage."""
    return render(request, 'tienda_bolis/home.html')