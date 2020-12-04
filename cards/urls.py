from django.urls import path
from .views import CardListView
from . import views

urlpatterns = [
    path('', CardListView.as_view(), name='cards-home'),
    path('about/', views.about, name='cards-about')
]
