#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    # here the order is important because it enables to use the default value in the view for page
    # this way we don't have to set a value for date in every template
    url(r'^$', views.documentList, name="DocumentList"),
    url(r'^id_cat(?P<cat_id>\d+)$', views.documentList, name="DocumentList"),
    url(r'^id_cat(?P<cat_id>\d+)p(?P<page>\d+)$', views.documentList, name="DocumentList"),
    url(r'^id_cat(?P<cat_id>\d+)p(?P<page>\d+)year(?P<year>\d+)$', views.documentList, name="DocumentList"),
]
