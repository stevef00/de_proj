from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from django.urls import reverse
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'cards/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'cards'
    ordering = ['-date_created']
    paginate_by = 1

class CardDetailView(DetailView):
    model = Card

class CardCreateView(LoginRequiredMixin, CreateView):
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

class CardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Card
    fields = ['front', 'back']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

    #
    # Determine the URL to redirect to when the form is successfully validated.
    # Returns success_url by default.
    #
    # FIXME: when we have Decks we'll want to redirect to the Deck
    # the card is added to.
    #
    def get_success_url(self):
        return reverse('cards-home')

class CardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Card
    success_url = '/' # FIXME: maybe we want to redirect somewhere else?

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'cards/about.html', {'title': 'About'})
