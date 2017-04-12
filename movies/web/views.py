# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
import requests
import traceback
from django.http import HttpResponse

from geopy.geocoders import Nominatim

from models import Movie
# Create your views here.

def api(request):
	query=request.GET.get('q','')
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
