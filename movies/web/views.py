# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
import requests
import traceback
from django.http import HttpResponse

from geopy.geocoders import Nominatim
# Create your views here.

def api(request):
	query=request.GET.get('q','')
	data_url='http://data.sfgov.org/resource/wwmu-gmzc.json'
	req=requests.get(data_url,verify=True)
	data=json.loads(req.text)

	for row in data:
		try:
			
			try:
				place=(row['locations']).encode('utf-8')
				geolocator = Nominatim()
				location = geolocator.geocode(str(place))
				lat=location.latitude
				lon=location.longitude
				print lat,lon
			except:
				print traceback.print_exc()	
		except:
			print traceback.print_exc()
