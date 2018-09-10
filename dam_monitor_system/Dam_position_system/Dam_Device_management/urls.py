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
import Dam_Device_management.views
import Displacement_management.views


urlpatterns = [
    url(r'^login/$', Dam_Device_management.views.login),

    url(r'^DandL_management/$', Dam_Device_management.views.DandL_management),
    url(r'^list_show/$', Dam_Device_management.views.List_show),

    url(r'^dam_management_form/$', Dam_Device_management.views.dam_management_form),
    url(r'^device_management_form/$', Dam_Device_management.views.device_management_form),
    url(r'^history_search/$', Displacement_management.views.history_search),
    url(r'^realTime_search/$', Displacement_management.views.realTime_search),

#大坝增删改查
    url(r'^add_form_Dam/$', Dam_Device_management.views.add_form_Dam),
    url(r'^dam_management_form/(?P<aid>\d+)/d/$', Dam_Device_management.views.delete_form_Dam),
    url(r'^dam_management_form_update/(?P<aid>\d+)/$', Dam_Device_management.views.dam_management_form_update),
    url(r'^dam_management_form_update/(?P<aid>\d+)/u/$', Dam_Device_management.views.update_form_Dam),

#设备增删改查
    url(r'^add_form_Device/$', Dam_Device_management.views.add_form_Device),
    url(r'^device_management_form/(?P<aid>\d+)/d/$', Dam_Device_management.views.delete_form_Device),
    url(r'^device_management_form_update/(?P<aid>\d+)/$', Dam_Device_management.views.device_management_form_update),
    url(r'^device_management_form_update/(?P<aid>\d+)/u/$', Dam_Device_management.views.update_form_Device),
]
