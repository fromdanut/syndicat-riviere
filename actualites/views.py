#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from models import Article
from django.db.models import Q
#from django.contrib.postgres.search import SearchVector, SearchQuery
from django.core.paginator import Paginator
from sivb.settings import ACTUALITE_PAGINATION_BY

# Create your views here.

def articleList(request, page):

    obj = Article.objects.all().order_by('-date') # queryset
    obj_paginated = Paginator(obj, ACTUALITE_PAGINATION_BY) # paginator instance
    """keep page_obj variable name for the pagination template to work"""
    page_obj = obj_paginated.page(page) # select the page with (?page) from urls.py

    # set a variable to controle the pagination in the template
    if page_obj.has_next :
        is_paginated = True

    return render(request, 'actualites/ArticleList.html', locals())

def articleSearch(request) :

    q = request.GET.get('q')

    foundArticles = Article.objects.filter(Q(contenu__search=q)|Q(titre__icontains=q)).order_by('-date')
    #foundArticles = Article.objects.annotate(search = SearchVector('contenu', 'titre', config='french'),).filter(search = SearchQuery(q, config='french')).order_by('-date')

    return render(request,'actualites/articleSearch.html', locals())
