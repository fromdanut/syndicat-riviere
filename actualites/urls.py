#-*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<page>[0-9]+)$', views.articleList, name = 'Actualite_ArticleList'),
    url(r'^search/', views.articleSearch, name = 'Actualite_articleSearch'),
]
