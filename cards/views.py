from django.shortcuts import render
from django.http import HttpResponse

cards = [
    {
        'owner': 'stevef',
        'front': 'the train station',
        'back':  'der Bahnhof',
        'date_created': 'December 1, 2020',
    },
    {
        'owner': 'stevef',
        'front': 'the car',
        'back':  'das Auto',
        'date_created': 'December 1, 2020',
    },
]

def home(request):
    context = {
        'cards': cards,
    }
    return render(request, 'cards/home.html', context)

def about(request):
    return render(request, 'cards/about.html', {'title': 'About'})
