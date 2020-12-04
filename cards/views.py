from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'cards/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'cards'
    ordering = ['-date_created']

class CardDetailView(DetailView):
    model = Card

class CardCreateView(CreateView):
    model = Card
    fields = ['front', 'back']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #
    # Determine the URL to redirect to when the form is successfully validated.
    # Returns success_url by default.
    #
    # FIXME: when we have Decks we'll want to redirect to the Deck
    # the card is added to.
    #
    def get_success_url(self):
        return reverse('cards-home')

def about(request):
    return render(request, 'cards/about.html', {'title': 'About'})
