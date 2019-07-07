# chat/urls.py

# from django.conf.urls import url
from django.urls import path, re_path

from . import views

# Added from video tutorial
app_name = 'chat'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.room, name='room'),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'), # Original line from actual tutorial
]
