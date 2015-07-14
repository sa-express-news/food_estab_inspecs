from django.conf.urls import patterns, url
from insps import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^(?P<estab_id>\d+)/$', views.estab, name='estab'),
    url(r'^(?P<inspection_key>\d+-\d+_\d+_\d+)/$', views.inspection, name='inspection'),
    url(r'^search/$', views.search, name='search'),
    )