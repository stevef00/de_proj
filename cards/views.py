from django.shortcuts import render
from django.http import HttpResponse
from .models import Card

def home(request):
    context = {
        'cards': Card.objects.all()
    }
    return render(request, 'cards/home.html', context)

def about(request):
    return render(request, 'cards/about.html', {'title': 'About'})
