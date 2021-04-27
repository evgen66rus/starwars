from django.shortcuts import render
from .models import Character, Planet
from django.views import generic
import requests, json
from django.http import HttpResponse

def index(request):
    return render(request, 'base_generic.html')

def character(request):
    person = Character.objects.all()
    context = {
        'person': person
    }
    return render(request, 'character.html', context=context)

def planets(request):
    residents = []
    planets = Planet.objects.all()
    context = {
        'planets': planets,
    }
    return render(request, 'planets.html', context=context)

def planet_detail_view(request,pk):
    try:
        planet_id=Planet.objects.get(pk=pk)
    except Planet.DoesNotExist:
        raise Http404("Planet does not exist")
    characters = Character.objects.filter(homeworld__name=planet_id)
    context = {
        'planet_id': planet_id,
        'characters': characters,
    }
    return render(request, 'planet-detail.html', context=context)

def update_data(request):
    # url = 'https://swapi.dev/api/people/1/'
    # zapros = requests.get(url)
    # zapros = zapros.json()

    url = 'https://swapi.dev/api'
    url_people = url + '/people'
    url_planets = url + '/planets'

    planets_data = requests.get(url_planets)
    planets_data = planets_data.json()['results']

    for parameters in planets_data:
        planet_name = parameters['name']
        planet_gravity = parameters['gravity']
        planet_climate = parameters['climate']
        planet_residents_urls = parameters['residents']
        char_list = []
        char_details = {}
        planet_data = {}
        for char_url in planet_residents_urls:
            char_raw_data = requests.get(char_url)
            char_raw_data = char_raw_data.json()
            char_name = char_raw_data['name']
            char_list.append(char_name)
            
            char_gender = char_raw_data['gender']
            char_details = {'name': char_name, 'homeworld': planet_name, 'gender': char_gender}
            #print(char_details)
        planet_data = {'name': planet_name, 'gravity': planet_gravity, 'climate': planet_climate, 'residents': char_list}
        #print(planet_data)



    html = "<html><body><pre>Data: %s.</pre></body></html>" % json.dumps(char_details, indent=2)
    return HttpResponse(html)