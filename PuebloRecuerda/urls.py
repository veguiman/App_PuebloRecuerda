# -*- coding: utf-8 -*-

<<<<<<< HEAD
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
=======

# Librerias Django:
from django.conf.urls import url
from django.conf.urls import include
>>>>>>> 1fbfc32c0a7f45fc4e88575e9da9a2975f3c4c72
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^diputados/', include('diputados.urls', namespace='diputados')),
=======
    url(r'^', include('home.urls', namespace='home')),
    url(r'^', include('seguridad.urls', namespace='seguridad')),
>>>>>>> 1fbfc32c0a7f45fc4e88575e9da9a2975f3c4c72
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
