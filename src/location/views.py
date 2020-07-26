from django.shortcuts import render
import json
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# Select2
def getCountry(request):

    if request.GET.get('search_c'):
        countries_db = Country.objects.filter(
            Q(name__iexact=request.GET.get('search_c')) | Q(name__icontains=request.GET.get('search_c'))
        )
    else:
        countries_db = Country.objects.all()

    countries = []

    for item in countries_db:
        countries.append({'id': item.id, 'text': item.name})

    arrs = {"results": countries}

    return JsonResponse(arrs)

def getRegion(request):

    if request.GET.get('search_r'):
        region_db = Region.objects.filter(
            Q(name__iexact=request.GET.get('search_r')) | Q(name__icontains=request.GET.get('search_r')), Q(country_id=request.GET.get('country_id'))
        )
    else:
        region_db = Region.objects.filter(country_id=request.GET.get('country_id'))

    regions = []

    for item in region_db:
        regions.append({'id': item.id, 'text': item.name})

    arrs = {"results": regions}

    return JsonResponse(arrs)

def getCity(request):

    if request.GET.get('search_city'):
        city_db = City.objects.filter(
            Q(name__iexact=request.GET.get('search_city')) | Q(name__icontains=request.GET.get('search_city')), Q(region_id=request.GET.get('region_id'))
        )
    else:
        city_db = City.objects.filter(region_id=request.GET.get('region_id'))
    cities = []

    for item in city_db:
        cities.append({'id': item.id, 'text': item.name})

    arrs = {
        "results": cities
    }

    return JsonResponse(arrs)

# получение для контента slug при изменение города
def get_city_slug(request):
    city = City.objects.filter(id=request.GET.get('city_id')).first()
    city_slug = city.slug
    return JsonResponse({'city_slug': city_slug})
