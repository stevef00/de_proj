from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>DE Cards Home</h1>')

def about(request):
    return HttpResponse('<h1>Put Cards About Page Here</h1>')
