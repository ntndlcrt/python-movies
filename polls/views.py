from django.shortcuts import render
import requests

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def all_view(request):
    data = requests.get('http://localhost:9000/all').json()
    return render(request, 'all.html', {'data': data})

def actors(request):
    data = requests.get('http://localhost:9000/actors/all').json()
    return render(request, 'actors.html', {'actors': data})
