# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.test import Client
from django.test import TestCase
from models import Movie

class ApiTest(TestCase):
	"""
	Testcases to check Movies Api
	"""
	def test1(self):
		url='http://127.0.0.1:8000/api/movies/'
		resp=requests.get(url)
		self.assertEqual(resp.status_code, 200)

	def test2(self):
		url='http://127.0.0.1:8000/api/movies/?title=180&year=2015'
		resp=requests.get(url)
		self.assertEqual(resp.status_code, 200)

	def test3(self):
		url='http://127.0.0.1:8000/api/movies/?actor2=Sharon Stone'
		resp=requests.get(url)
		self.assertEqual(resp.status_code, 200)

	def test4(self):
		url='http://127.0.0.1:8000/api/movies/?production=SPI Cinemas'
		resp=requests.get(url)
		self.assertEqual(resp.status_code, 200)

	def test5(self):
		obj=Movie(title='new_title',director='dir',lat=0.0,lon=0.0,locations='loc')
		obj.save()
		obj=Movie.objects.get(locations='loc')
		self.assertEqual(obj.title,"new_title")


