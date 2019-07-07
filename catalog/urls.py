from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views
from chat import views as chat_views
# import chat.views.messages

urlpatterns = [
    path('', RedirectView.as_view(url='/LIVE/', permanent=True)),
    path('LIVE/', views.LocationListView.as_view(), name='LIVE'),
    path('Cafeteria', views.cafeteria_form, name='cafeteria_form'),
    path('EastLobby/', views.east_lobby_form, name='east_lobby_form'),
    path('TownCentre/', views.town_centre_form, name='town_centre_form'),
    path('About/', views.about, name='about'),
    path('LIVE/CodeRedStatus/', views.code_red_status, name='code_red_status_view'),
    re_path(r'^.*CodeRed.*$', views.code_red_status, name='code_red_status'),
    re_path(r'^.*Messages.*$', chat_views.messages, name='messages_2'),

    # re_path(r'^.*Messages.*$', views')
    # path('catalog/', RedirectView.as_view(url='/Home/LIVE/', permanent=True))
]
