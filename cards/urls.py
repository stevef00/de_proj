from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cards-home'),
    path('about/', views.about, name='cards-about')
]
