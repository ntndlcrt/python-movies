from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def all_view(request):
    response_genres = requests.get('http://localhost:9000/genres').json()
    genres = response_genres['genres']

    response_countries = requests.get('http://localhost:9000/countries').json()
    countries = response_countries['countries']

    response_release_years = requests.get('http://localhost:9000/release_years').json()
    release_years = response_release_years['release_years']

    # response_predict = requests.get('http://localhost:9000/predict').json()
    # predict = response_predict['predict']

    # My all.html view has a form with a POST method that expects a result returned by http://localhost:9000/predict route. I want to check if the form was submotted and, if yes, give its response to the template

    api_data = ''
    if request.method == 'POST':
        genre = request.POST.get('genre')
        country = request.POST.get('country')
        release_year = request.POST.get('release_year')

        response = requests.post('http://localhost:9000/predict', json={'genre': genre, 'country': country, 'release_year': release_year})

        if response.status_code == 200:
            api_data = response.json()

    context = {'genres': genres, 'countries': countries, 'release_years': release_years, 'api_data': api_data}

    return render(request, 'all.html', context)

def actors(request):
    data = requests.get('http://localhost:9000/actors/all').json()
    return render(request, 'actors.html', {'actors': data})
