from django.urls import path
from .views import CardListView, CardDetailView
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='cards-home'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('about/', views.about, name='cards-about')
]
