"""Views for the photo showcase application."""

from django.shortcuts import render


def home(request):
    """Render the photo showcase page."""
    return render(request, 'escaparate/home.html')
