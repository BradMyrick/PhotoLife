from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def explore(request):
    """Renders the explore page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '../templates/portfolio.html',
        {
            'title': 'Explore Page',
            'year':datetime.now().year,
            }
        )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '../templates/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

