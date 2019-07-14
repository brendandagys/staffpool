"""staff_pool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.conf.urls import include, url
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

from chat.views import messages, chat_session_name
from catalog.views import homepage
from catalog.views import session_name

urlpatterns = [
    re_path(r'.*ChatSession.*', chat_session_name, name='chat_session_name'),
    path('admin/', admin.site.urls, name='admin'),
    re_path(r'^.*Messages.*$', messages, name='messages'),
    # path('chat/', include('chat.urls')),
    re_path(r'^.*chat.*', include('chat.urls')),
    re_path(r'^.*Session.*$', session_name, name='session_name'),

    path('', homepage, name='homepage'),
    path('messages/', include('chat.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # Add Django site authentication urls (for login, logout, password management)
    path('CodeRed/', include('catalog.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
