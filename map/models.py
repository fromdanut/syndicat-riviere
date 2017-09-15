#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class BassinVersant(models.Model):
    code_zone = models.CharField(max_length=4)
    libelle = models.CharField(max_length=125)
    id_nd_exut = models.BigIntegerField()
    c_hyd_cdo = models.CharField(max_length=8)
    pkhexut = models.IntegerField()
    lib_ss_sec = models.CharField(max_length=125)
    lib_sect = models.CharField(max_length=125)
    lib_region = models.CharField(max_length=125)
    geom = models.PolygonField(srid=2154)

# Auto-generated `LayerMapping` dictionary for BassinVersant model
bassinversant_mapping = {
    'code_zone' : 'CODE_ZONE',
    'libelle' : 'LIBELLE',
    'id_nd_exut' : 'ID_ND_EXUT',
    'c_hyd_cdo' : 'C_HYD_CDO',
    'pkhexut' : 'PKHEXUT',
    'lib_ss_sec' : 'LIB_SS_SEC',
    'lib_sect' : 'LIB_SECT',
    'lib_region' : 'LIB_REGION',
    'geom' : 'POLYGON25D',
}

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Cdo(models.Model):
    code_hydro = models.CharField(max_length=8)
    toponyme = models.CharField(max_length=127)
    geom = models.MultiLineStringField(srid=2154)
    ordre = models.IntegerField(null=True, blank = True)

# Auto-generated `LayerMapping` dictionary for Cdo model
cdo_mapping = {
    'code_hydro' : 'CODE_HYDRO',
    'toponyme' : 'TOPONYME',
    'geom' : 'MULTILINESTRING25D',
}

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Clc(models.Model):
    code_12 = models.CharField(max_length=3)
    geom = models.MultiPolygonField(srid=2154)

# Auto-generated `LayerMapping` dictionary for Clc model
clc_mapping = {
    'code_12' : 'code_12',
    'geom' : 'MULTIPOLYGON',
}

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Step(models.Model):
    bassin_cod = models.CharField(max_length=2)
    region_nom = models.CharField(max_length=17)
    departemen = models.CharField(max_length=2)
    code_uh = models.CharField(max_length=50)
    nom_uh = models.CharField(max_length=80)
    agglo_code = models.CharField(max_length=12)
    agglo_nom = models.CharField(max_length=48)
    nbre_step = models.FloatField()
    nbre_step_field = models.FloatField()
    taille_agg = models.FloatField()
    step_code = models.CharField(max_length=12)
    step_nom = models.CharField(max_length=48)
    coord_x_de = models.FloatField()
    coord_y_de = models.FloatField()
    step_activ = models.CharField(max_length=3)
    geom = models.MultiPointField(srid=2154)

# Auto-generated `LayerMapping` dictionary for Step model
step_mapping = {
    'bassin_cod' : 'Bassin_cod',
    'region_nom' : 'Region_nom',
    'departemen' : 'Departemen',
    'code_uh' : 'Code_UH',
    'nom_uh' : 'Nom_UH',
    'agglo_code' : 'Agglo_Code',
    'agglo_nom' : 'Agglo_nom',
    'nbre_step' : 'Nbre_STEP',
    'nbre_step_field' : 'Nbre_STEP_',
    'taille_agg' : 'Taille_agg',
    'step_code' : 'STEP_code',
    'step_nom' : 'STEP_nom',
    'coord_x_de' : 'Coord_X_de',
    'coord_y_de' : 'Coord_Y_de',
    'step_activ' : 'STEP_activ',
    'geom' : 'MULTIPOINT',
}

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Captage(models.Model):
    nom_com = models.CharField(max_length=50)
    nbre_capta = models.BigIntegerField()
    type = models.CharField(max_length=10)
    geom = models.MultiPointField(srid=2154)

# Auto-generated `LayerMapping` dictionary for Captage model
captage_mapping = {
    'nom_com' : 'NOM_COM',
    'nbre_capta' : 'Nbre_Capta',
    'type' : 'type',
    'geom' : 'MULTIPOINT',
}




