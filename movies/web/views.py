# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
import requests
import traceback

from geopy.geocoders import Nominatim

from models import Movie
from django.http import HttpResponse
from rest_framework import filters
from rest_framework import serializers,viewsets
from django_filters.rest_framework import DjangoFilterBackend


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """
    Movie Serializer to Serialize mention fields
    """
    class Meta:
        model=Movie
        fields=('title','year','lat','lon','director','writer',
        'actor1','actor2','actor3','production','locations')

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields=('title','year','lat','lon','director','writer',
        'actor1','actor2','actor3','production','locations')

def home(request):
    query=request.GET.get('q',None)
    print 'query',query
    api_url='http://127.0.0.1:8000/api/movies/'
    if query is not None:
        api_url=query
    req=requests.get(api_url)
    data=json.loads(req.text)
    return render(request, "home.html",{'data':data})

def scrape(request):
    """
    Method to read datasf api and store it into db, not using datasf api directly to avoid 
    duplicates(since, there were many).
    """
    data_url='http://data.sfgov.org/resource/wwmu-gmzc.json'
    req=requests.get(data_url,verify=True)
    data=json.loads(req.text)

    for row in data:
        try:
            title=row.get('title')
            year=row.get('release_year',None)
            writer=row.get('writer',None)
            production=row.get('production_company',None)
            director=row.get('director',None)
            actor1=row.get('actor_1',None)
            actor2=row.get('actor_2',None)
            actor3=row.get('actor_3',None)
            locations=row.get('locations',None)
            try:
                place=row.get('locations',None)
                geolocator = Nominatim()
                location = geolocator.geocode(str(place))
                lat=location.latitude
                lon=location.longitude
            except:
                lat=0.0     #geolocator didn't return any location obj 
                lon=0.0     #geolocator didn't return any location obj
                print traceback.print_exc()
            movie_obj=Movie(title=title,year=year,director=director,writer=writer,production=production
                ,actor1=actor1,actor2=actor2,actor3=actor3,lat=lat,lon=lon,locations=locations) 
            movie_obj.save()
        except:
            print traceback.print_exc()
