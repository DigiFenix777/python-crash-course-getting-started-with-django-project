from django.shortcuts import render

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzeria/index.html')

