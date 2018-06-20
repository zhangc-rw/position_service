"""Dam_position_system URL Configuration

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
import Displacement_management.views

urlpatterns = [
    url(r'^DReal_management/$', Displacement_management.views.DReal_management),
    #url(r'^DPast_management/$', Displacement_management.views.DPast_management),

    url(r'^label_detail_realtime/(?P<aid>\d+)/(?P<bid>\d+)/$', Displacement_management.views.DReal_management),
    url(r'^label_history_select/(?P<aid>\d+)/(?P<bid>\d+)/$', Displacement_management.views.label_history_select),
    url(r'^label_detail_history/(?P<aid>\d+)/(?P<bid>\d+)/$', Displacement_management.views.DPast_management),
]
