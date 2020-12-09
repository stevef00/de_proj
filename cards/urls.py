from django.urls import path
from .views import (
        CardListView,
        CardDetailView,
        CardCreateView,
        CardUpdateView,
        CardDeleteView,
        UserCardListView,
        DeckListView,
        DeckDetailView,
        DeckCreateView,
        DeckUpdateView,
        DeckDeleteView
)
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='cards-home'),
    path('user/<str:username>/', UserCardListView.as_view(), name='user-cards'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('card/new/', CardCreateView.as_view(), name='card-create'),
    path('card/<int:pk>/update/', CardUpdateView.as_view(), name='card-update'),
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card-delete'),
    path('about/', views.about, name='cards-about'),
    path('deck/', DeckListView.as_view(), name='deck-list'),
    path('deck/<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('deck/<int:pk>/update/', DeckUpdateView.as_view(), name='deck-update'),
    path('deck/<int:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
    path('deck/new/', DeckCreateView.as_view(), name='deck-create')
]
