from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'cards/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'cards'
    ordering = ['-date_created']

def about(request):
    return render(request, 'cards/about.html', {'title': 'About'})
