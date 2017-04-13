# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
import requests
import traceback

from geopy.geocoders import Nominatim

from web import logger
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
    try:
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer
        #initialising filter backend for MovieViewSet
        filter_backends = [filters.DjangoFilterBackend]
        #declaring filter field for api          
        filter_fields=('title','year','lat','lon','director','writer',
            'actor1','actor2','actor3','production','locations')
    except:
        tb=traceback.print_exc()
        logger.err(tb)  

        
def home(request):
    """
    Method to show default home page, fetching data from 
    paginated api of size 10
    """
    try:
        query=request.GET.get('q',None)
        api_url='http://127.0.0.1:8000/api/movies/'
        if query is not None:
            api_url=query
            logger.info("showing default home page")
        logger.info(api_url)
        req=requests.get(api_url)
        data=json.loads(req.text)
        #rendering home.html with data from api
        return render(request, "home.html",{'data':data})
    except:
        tb=traceback.print_exc()
        logger.err(tb)   
        
def scrape(request):
    """
    Method to read datasf api and store it into db, not using 
    datasf api directly to avoid duplicates(since, there were many).
    """
    try:
        logger.info("Reading datasf api....")
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
                except:     #error in fetching lat & lon
                    lat=0.0     #geolocator didn't return any location obj 
                    lon=0.0     #geolocator didn't return any location obj
                    tb=traceback.print_exc()
                    logger.err(tb)
                
                try:    
                    movie_obj=Movie(title=title,year=year,director=director
                        ,writer=writer,production=production,actor1=actor1,actor2=actor2,
                        actor3=actor3,lat=lat,lon=lon,locations=locations) 
                    movie_obj.save()    #saving movie object instance
                    logger.info("movie obj successfully saved")
                except:     #some error occured while saving movie object instance
                    tb=traceback.print_exc()
                    logger.err(tb)

            except:       #error while reading an entry from datasf json
                logger.err(tb)
                tb=traceback.print_exc()

    except:     #error in accessing datasf api
        tb=traceback.print_exc()
        logger.err(tb)
