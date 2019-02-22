from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^loadpage/$', loadPage, name='loadpage'),
    url(r'^word/$', word, name='word'),
]