from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^loadanimal/$', loadanimal, name='loadanimal'),
    url(r'^getmg/$', getmg, name='getmg'),
]