#-*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.flatpages import views as flatpagesViews

urlpatterns = [
    url(r'^$', flatpagesViews.flatpage, {'url': '/accueil/'}, name='accueil'),
    url(r'^admin/', admin.site.urls),
    url(r'^actualites/', include('actualites.urls')),
    url(r'^archives/', include('archives.urls')),
    url(r'^map/', include('map.urls')),
]

# in order to display flatpages
urlpatterns += [ url(r'^(?P<url>.*/)$', flatpagesViews.flatpage), ]

#staticfiles
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

# mediafiles
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
