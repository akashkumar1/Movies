# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
	"""
	Declaring Movie model fields
	"""
	title=models.CharField(max_length=100)
	year=models.IntegerField(null=True,blank=True)
	locations=models.CharField(max_length=250)
	#latitude calculated using geopy on locations attribute
	lat=models.FloatField()
	#longitude calculated using geopy on locations attribute		
	lon=models.FloatField()
	writer=models.CharField(max_length=100,null=True,blank=True)
	production=models.CharField(max_length=250,null=True,blank=True)
	director=models.CharField(max_length=100)
	actor1=models.CharField(max_length=100,null=True,blank=True)
	actor2=models.CharField(max_length=100,null=True,blank=True)
	actor3=models.CharField(max_length=100,null=True,blank=True)

	class Meta:
		"""
		unique together constraint to avoid duplicates while reading
		datasf api.Also, because a director will not make a movie with 
		a same title.
		"""
		unique_together=(('title','director'))