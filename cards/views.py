from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'cards/home.html')

def about(request):
    return HttpResponse('<h1>Put Cards About Page Here</h1>')
