from django.shortcuts import render
from .models import Character, Planet
from django.views import generic

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