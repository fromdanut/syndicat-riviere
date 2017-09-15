#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from archives.models import Categorie, Document
from django.core.paginator import Paginator

# Create your views here.

def documentList(request, cat_id='0', page='1', year='0'):

    # fetch the informations for the dropdown menu
    Categories = Categorie.objects.all() # for the categorie.name

    if cat_id == '0' : 
        currentCategorieName = 'Catégories'
    else : # set a str variable to the current categorie searched
	# filter by id, fetch only the column 'nom' and the distinct value
        currentCategorieName = Categorie.objects.filter(id=cat_id).values('nom').distinct()
	# in the end we have a queryset with only 1 value that
	# we retrieve to send a str obj to the template
        currentCategorieName = currentCategorieName[0]['nom']

    Dates = Document.objects.datetimes('date', 'year', order='DESC')
    Years = list() # the list that will be used in the template
    for date in Dates : # to fetch all distinct years of each document
        if date not in Years :
            Years.append(date)

    # first part of the queryset 
    if cat_id == '0' : # to fetch all categories
        obj = Document.objects.all()
    else :
        obj = Document.objects.filter(categorie__id=cat_id)

    # second part of the queryset : "filter date" and "order by"
    if year == '0' : #special value to fetch all years
        obj = obj.order_by('-date') # without filter...
    else :
        obj = obj.filter(date__year=year).order_by('-date') # filter by year

    # pagination
    PAGINATION_BY = 10 # modifiable
    obj_paginated = Paginator(obj, PAGINATION_BY) 
    """keep page_obj variable name for the pagination template to work"""
    page_obj = obj_paginated.page(page) # select the page with (?page) from urls.py
       
    # set a variable 'is_paginated' to controle the pagination in the template
    if page_obj.has_next :
        is_paginated = True

    # DEBUG set a more explicite name to cat_id for the template to be clearer !
    cat_id_from_view = cat_id

    return render(request, 'archives/documents_list.html', locals())
