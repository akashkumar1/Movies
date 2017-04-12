# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	list_display=('title','year','lat','lon','director','writer',
		'actor1','actor2','actor3','production')
	search_fields=['title','year','lat','lon','director','writer',
	'actor1','actor2','actor3','production']
admin.site.register(Movie,MovieAdmin)	

