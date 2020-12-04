from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'cards/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'cards'
    ordering = ['-date_created']

class CardDetailView(DetailView):
    model = Card

def about(request):
    return render(request, 'cards/about.html', {'title': 'About'})
