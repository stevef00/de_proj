from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from django.urls import reverse
from cards.models import Deck, Card

class DeckListView(ListView):
    model = Deck
    template_name = 'cards/deck_list.html'
    context_object_name = 'decks'
    ordering = ['-date_created']

class DeckDetailView(DetailView):
    model = Deck

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the cards
        #deck = Deck.objects.filter(id=pk).first()
        context['cards'] = Card.objects.filter(deck=context['deck'])
        return context


class DeckCreateView(LoginRequiredMixin, CreateView):
    model = Deck
    fields = ['deck_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('deck-list')

class DeckUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Deck
    fields = ['deck_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        deck = self.get_object()
        if self.request.user == deck.author:
            return True
        else:
            return False

    #
    # Determine the URL to redirect to when the form is successfully validated.
    # Returns success_url by default.
    #
    def get_success_url(self):
        return reverse('deck-list')

class DeckDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Deck
    success_url = '/deck' # FIXME: maybe we want to redirect somewhere else?

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
