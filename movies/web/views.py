# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
import requests
import traceback
from django.http import HttpResponse

from geopy.geocoders import Nominatim

from models import Movie
from rest_framework import serializers,viewsets
from django_filters.rest_framework import DjangoFilterBackend

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Movie
        fields=('title','year','lat','lon','director','writer',
		'actor1','actor2','actor3','production')

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend,)
    # filter_fields=('title',)
    # filter_fields =('title','year','lat','lon','director','writer',
		# 'actor1','actor2','actor3','production')

def home(request):
	query=request.GET.get('q',None)
	api_url='http://127.0.0.1:8000/api/movies/'
	req=requests.get(api_url)
	data=json.loads(req.text)
	# print data
	return render(request, "home.html",{'data':data})

def scrape(request):
	data_url='http://data.sfgov.org/resource/wwmu-gmzc.json'
	req=requests.get(data_url,verify=True)
	data=json.loads(req.text)

	for row in data:
		try:
			title=(row['title']).encode('utf-8')
			year=(row['release_year']).encode('utf-8') if row['release_year'] else None
			writer=(row['writer']).encode('utf-8') if row['writer'] else None
			production=(row['production_company']).encode('utf-8') if row['production_company'] else None
			director=(row['director']).encode('utf-8')
			actor1=(row['actor_1']).encode('utf-8')	if row['actor_1'] else None
			actor2=(row['actor_2']).encode('utf-8') if row['actor_2'] else None
			actor3=(row['actor_3']).encode('utf-8') if row['actor_3'] else None
			try:
				place=(row['locations']).encode('utf-8')
				geolocator = Nominatim()
				location = geolocator.geocode(str(place))
				lat=location.latitude
				lon=location.longitude
			except:
				lat=0.0		#geolocator didn't return any location obj 
				lon=0.0		#geolocator didn't return any location obj
				print traceback.print_exc()
			movie_obj=Movie(title=title,year=year,director=director,writer=writer,production=production
				,actor1=actor1,actor2=actor2,actor3=actor3,lat=lat,lon=lon)	
			movie_obj.save()
		except:
			print traceback.print_exc()
