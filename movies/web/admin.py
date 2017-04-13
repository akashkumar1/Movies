# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Movie
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
	"""
	Adding display fields & search fields for admin panels
	"""
	list_display=('title','year','lat','lon','director','writer',
		'actor1','actor2','actor3','production','locations')
	search_fields=['title','year','lat','lon','director','writer',
	'actor1','actor2','actor3','production','locations']
admin.site.register(Movie,MovieAdmin)	

