# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
	title=models.CharField(max_length=100)
	year=models.IntegerField()
	lat=models.FloatField()
	lon=models.FloatField()
	writer=models.CharField(max_length=100)
	production=models.CharField(max_length=100)
	director=models.CharField(max_length=100)
	actor1=models.CharField(max_length=100)
	actor2=models.CharField(max_length=100)
	actor3=models.CharField(max_length=100)

