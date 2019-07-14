# chat/urls.py

# from django.conf.urls import url
from django.urls import path, re_path

from . import views
# from catalog.views import session_name

# Added from video tutorial
app_name = 'chat'

urlpatterns = [
    # path('', views.index, name='index'),
    re_path('ChatSession/', views.chat_session_name, name ='chat_session_name'),

    path('', views.room, name='room'),
    # re_path(r'.*Session.*', catalog_views.session_name, name ='session_name'),

    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'), # Original line from actual tutorial
]
