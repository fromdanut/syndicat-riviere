#-*- coding: utf-8 -*-

import os
from django.contrib.gis.utils import LayerMapping
from .models import Step, step_mapping, Captage, captage_mapping





CAPTAGE_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'captage.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        Captage, CAPTAGE_shp, captage_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)






"""
IPR_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'IPR.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        Ipr, IPR_shp, ipr_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)
"""
