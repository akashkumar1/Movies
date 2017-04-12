# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
	title=models.CharField(max_length=100)
	year=models.IntegerField(null=True,blank=True)
	lat=models.FloatField()
	lon=models.FloatField()
	writer=models.CharField(max_length=100,null=True,blank=True)
	production=models.CharField(max_length=100,null=True,blank=True)
	director=models.CharField(max_length=100)
	actor1=models.CharField(max_length=100,null=True,blank=True)
	actor2=models.CharField(max_length=100,null=True,blank=True)
	actor3=models.CharField(max_length=100,null=True,blank=True)

	class Meta:
		unique_together=(('title','director'))			# To avoid duplicate entries from api