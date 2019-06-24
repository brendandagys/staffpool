from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('Cafeteria', views.cafeteria_form, name='cafeteria_form'),
    path('EastLobby/', views.east_lobby_form, name='east_lobby_form'),
    path('TownCentre/', views.town_centre_form, name='town_centre_form'),
    path('LIVE/', views.LocationListView.as_view(), name='LIVE'),
    path('About/', views.about, name='about'),
    path('', RedirectView.as_view(url='/Home/LIVE/', permanent=True)),
]
