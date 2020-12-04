from django.urls import path
from .views import (
        CardListView,
        CardDetailView,
        CardCreateView,
        CardUpdateView
)
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='cards-home'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('card/new/', CardCreateView.as_view(), name='card-create'),
    path('card/update/<int:pk>/', CardUpdateView.as_view(), name='card-update'),
    path('about/', views.about, name='cards-about')
]
