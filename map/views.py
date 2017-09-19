#-*- coding: utf-8 -*-

from django.shortcuts import render
from .models import BassinVersant, Cdo, Clc, Step, Captage

# to load data from the db into the template cf. Djangoproject doc and especially GeoJson Serializer
from django.core.serializers import serialize 

# Create your views here.

def showMap(request):

    def setData(querryset) :
	"""to generate Json string object for JS leaflet in template"""
        geojson_data = serialize('geojson', querryset)
        geojson_data_string = str(geojson_data)
        return geojson_data_string

    BV = setData(BassinVersant.objects.all())
    CDO = setData(Cdo.objects.all())
    CLC = setData(Clc.objects.all())
    STEP = setData(Step.objects.all())
    CAPTAGE = setData(Captage.objects.all())

    return render(request,'map/map.html', locals())
