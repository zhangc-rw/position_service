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

    url(r'^PandG_management/$', carrier_management.views.PandG_management),
    url(r'^personnel_management_form/$', carrier_management.views.personnel_management_form),
    url(r'^gun_management_form/$', carrier_management.views.gun_management_form),

    url(r'^add_form_person/$', carrier_management.views.add_form_PG),
    url(r'^personnel_management_form/(?P<aid>\d+)/d/$', carrier_management.views.delete_form_PG),
    url(r'^personnel_management_form_update/(?P<aid>\d+)/u/$', carrier_management.views.update_form_PG),
    url(r'^personnel_management_form_update/(?P<aid>\d+)/$', carrier_management.views.personnel_management_form_update),
    
    url(r'^add_form_gun/$', carrier_management.views.add_form_PG),
    url(r'^gun_management_form_update/(?P<aid>\d+)/$', carrier_management.views.gun_management_form_update),
    url(r'^gun_management_form/(?P<aid>\d+)/d/$', carrier_management.views.delete_form_PG),
    url(r'^gun_management_form_update/(?P<aid>\d+)/u/$', carrier_management.views.update_form_PG)


    
    ]
