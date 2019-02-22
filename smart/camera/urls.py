from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^camera/$', loadImage, name='camera'),
    url(r'^face/$', getFace, name='face')
]