from django.urls import path
from .views import (
        CardListView,
        CardDetailView,
        CardCreateView,
        CardUpdateView,
        CardDeleteView,
        UserCardListView
)
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='cards-home'),
    path('user/<str:username>/', UserCardListView.as_view(), name='user-cards'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('card/new/', CardCreateView.as_view(), name='card-create'),
    path('card/<int:pk>/update/', CardUpdateView.as_view(), name='card-update'),
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card-delete'),
    path('about/', views.about, name='cards-about')
]
