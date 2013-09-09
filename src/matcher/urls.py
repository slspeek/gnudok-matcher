""" Url configuration """
from __future__ import absolute_import
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf.urls import patterns, include, url
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/doc/',
                        include('django.contrib.admindocs.urls')),
                       (r'^admin/',
                        include(admin.site.urls)),
                       )
urlpatterns += staticfiles_urlpatterns()
