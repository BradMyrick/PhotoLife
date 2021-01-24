from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

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


def profile(request):
    """Renders the profile page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '../templates/profile.html',
        {
            'title':'Profile Page',
            'year':datetime.now().year,
        }
    )

def notifications(request):
    """Renders the notifications page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '../templates/notifications.html',
        {
            'title':'Notifications Page',
            'year':datetime.now().year,
        }
    )

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

def signup(request):
    """Renders the explore page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '../templates/signup.html',
        {
            'title': 'Signup Page',
            'year':datetime.now().year,
            }
        )



