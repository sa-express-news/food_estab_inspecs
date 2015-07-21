from django.conf.urls import patterns, include, url
from insps import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'insps.views.index', name='index'),
    url(r'^(?P<estab_id>\d+)/$', views.estab, name='estab'),
    url(r'^(?P<inspection_key>\d+-\d+_\d+_\d+)/$', views.inspection, name='inspection'),
    url(r'^search/$', views.search, name='search'),
    url(r'^admin/', include(admin.site.urls)),
)
