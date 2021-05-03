from django.shortcuts import render
from .models import Character, Planet
from django.views import generic
import requests, json
from django.http import HttpResponse, Http404

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
    # fetching data from the api
    
    url = 'https://swapi.dev/api'
    url_people = url + '/people'
    url_planets = url + '/planets'
    planets_data = requests.get(url_planets)
    planets_data = planets_data.json()['results']

    char_data = requests.get(url_people)
    char_data = char_data.json()['results']
    for char in char_data:
        char_name = char['name']
        if Character.objects.filter(name=char_name):
            continue
        else:
            for parameters in planets_data:
                planet_name = parameters['name']
                planet_gravity = parameters['gravity']
                planet_climate = parameters['climate']
                planet_residents_urls = parameters['residents']
                char_list = []
                char_details = {}
                planet_data = {'name': planet_name, 'gravity': planet_gravity, 'climate': planet_climate}
                planets_in_db = 0
                planets_updated = 0

                if Planet.objects.filter(name=planet_name):
                    continue
                else:
                    p = Planet.objects.create(name=planet_name, gravity=planet_gravity, climate=planet_climate)
                    p.save()
                
                for char_url in planet_residents_urls:
                    char_raw_data = requests.get(char_url)
                    char_raw_data = char_raw_data.json()
                    char_homeworld = planet_name
                    char_name = char_raw_data['name']
                    char_gender = char_raw_data['gender']
                    char_details = {'name': char_name, 'homeworld': char_homeworld, 'gender': char_gender}
                    char_in_db = 0
                    char_updated = 0
                    if Character.objects.filter(name=char_name):
                        char_in_db += 1
                    else:
                        homeworld_id = Planet.objects.get(name=char_homeworld)
                        homeworld_id = homeworld_id.pk
                        c = Character.objects.create(name=char_name, gender=char_gender, homeworld=Planet.objects.get(pk=homeworld_id))
                        c.save()
                        char_updated += 1

    return render(request, 'update_data.html')