from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^story/$', story, name='story'),
    url(r'^talk/$', talk, name='talk'),
]