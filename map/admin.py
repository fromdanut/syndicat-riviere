#-*- coding: utf-8 -*-

from django.contrib.gis import admin
from .models import BassinVersant, Cdo, Clc, Step, Captage

for model in BassinVersant, Clc, Step, Captage :
    admin.site.register(model, admin.OSMGeoAdmin)

class CdoAdmin(admin.OSMGeoAdmin):

    list_display   = ('toponyme', 'code_hydro', 'ordre',)

    fieldsets = (
			('General info', {
				'description' : 'general info',
				'fields' : ('toponyme', 'code_hydro', 'ordre', 'geom',)
		      		         }
			),
		) 

admin.site.register(Cdo, CdoAdmin)
