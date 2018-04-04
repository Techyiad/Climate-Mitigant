"""
Definition of views.
"""

from __future__ import absolute_import, division, print_function, unicode_literals
import config
from django.shortcuts import render, HttpResponse
from django.http import HttpRequest, JsonResponse
from django.template import RequestContext
import ee
import datetime as dt
import types   
import os
import json

##############################################################################
#                               Initialization.                               #
###############################################################################

#############################

ee.Initialize(config.credentials)

from app.dataset_processor import _Getcollection, chart_it, _ReadOptions, palletedata
from app.drought import  indices
from app.series import Options, timelapse_data






def home(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/index.html'
	)

def mail(request):
	"""Renders the contact page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/mail.html'
	)
global palettechoice
def about(request):
	"""Renders the about page."""
	assert isinstance(request, HttpRequest)
	return render(  request, 'app/about.html' )

def calcdata(request):

	
	global data,palettedecide
	if(request.method=="POST"):
		options= _ReadOptions(request)
		print(options)
		if options["dataset"]=='NDVI':
			palettedecide='NDVI'
		elif options["dataset"]=='EVI':
			palettedecide='EVI'
		elif options["dataset"]=='NDWI':
			palettedecide='NDWI'
		palete=palletedata(palettedecide,None)
		data=_Getcollection(options,palete)
	return JsonResponse(data)
		
	


def indices_compute(request):
	global data
	if(request.method=="POST"):
		options= _ReadOptions(request)
		data=indices(options)		
	return JsonResponse(data)


def indices_download(request):
	global data
	if(request.method=="POST"):
		options= _ReadOptions(request)
		data=indices(options)		
	return JsonResponse(data)



def timeseries(request):
	global data
	if(request.method=="POST"):
		try:
			options= Options(request)
			print(options)
			data=timelapse_data(options) 
		except  ee.EEException as ex:
			data={'error':'Failed to Compute Time Series . Error Stated::, '+str(ex)}
			pass
		

		
	return JsonResponse(data)




def map1(request):
	global data
	if(request.method=="POST"):
		options= _ReadOptions(request)
		data=indices(options)

	return JsonResponse(data)

def map2(request):
	global data
	if(request.method=="POST"):
		options= _ReadOptions(request)
		data=indices(options)
		
	return JsonResponse(data)


def map3(request):
	global data
	if(request.method=="POST"):
		options= _ReadOptions(request)
		
		data=indices(options)	
	return JsonResponse(data)



def map4(request):
	global data
	if(request.method=="POST"):
		options= _ReadOptions(request)
		data=indices(options)	
	return JsonResponse(data)




def download_data(request):
	try:
		global data,palettedecide
		if(request.method=="POST"):
			options= _ReadOptions(request)
			if options["dataset"]=='NDVI':
				palettedecide='NDVI'
			elif options["dataset"]=='EVI':
				palettedecide='EVI'
			elif options["dataset"]=='NDWI':
				palettedecide='NDWI'
			palete=palletedata(palettedecide,None)
			data= _Getcollection(options,palete)

	except ee.EEException as e:
			data={'error':'Failed to Download Data . Error Stated::, '+str(e)}	
	return JsonResponse(data)	

def chart_data(request):
	try:
		global data,palettedecide
		if(request.method=="POST"):
			options= _ReadOptions(request)
			if options["dataset"]=='NDVI':
				palettedecide='NDVI'
			elif options["dataset"]=='EVI':
				palettedecide='EVI'
			elif options["dataset"]=='NDWI':
				palettedecide='NDWI'
			palete=palletedata(palettedecide,None)
			data= chart_it(options,palete)

		
	except ee.EEException as e:
			data={'error':'Failed to Compute  Data . Error Stated::, '+str(e)}
	return JsonResponse(data)
		




def cal_drought(request):
	 global data , options , year , month
	 
	 
	 if(request.method=="POST"):
		 year=request.POST.get('useryear')
		 month=request.POST.get('usermonth')
		 
		 data = dodrought(request,year,month)
	 return JsonResponse(data)



def dataset(request):

	"""Renders the about page."""     
	assert isinstance(request, HttpRequest) 
	return render(
		request,
		'app/dataset.html') 
	


def compare(request):
	"""Renders the about page."""
	assert isinstance(request, HttpRequest)

	return render(  request, 'app/compare.html')
