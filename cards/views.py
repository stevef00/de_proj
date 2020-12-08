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
from .models import Card

class CardListView(ListView):
    model = Card
    template_name = 'cards/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'cards'
    ordering = ['-date_created']
    paginate_by = 1

class UserCardListView(ListView):
    model = Card
    template_name = 'cards/user_cards.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'cards'
    paginate_by = 1

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Card.objects.filter(author=user).order_by('-date_created')


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
