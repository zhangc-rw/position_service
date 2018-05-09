"""NBIOT_position_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import real_time_monitoring.views
import carrier_management.views


urlpatterns = [

    url(r'^track_the_playback/$', real_time_monitoring.views.track_the_playback),
    url(r'^real_time_monitoring/$', real_time_monitoring.views.real_time_monitoring,name='tiao'),

    url(r'^postdata/$', real_time_monitoring.views.postdata),
    url(r'^postdata1/$', real_time_monitoring.views.postdata1),

    url(r'^canvas_realTime/$', real_time_monitoring.views.canvas_realTime)
    
    ]
