from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^loadman/$', loadman, name='loadman'),
    url(r'^getmsg/$', getmsg, name='getmsg'),

]