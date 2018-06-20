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
from django.conf.urls import url,include
from django.contrib import admin
import Dam_Device_management.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Dam_Device_management.views.DandL_management),
    url(r'^Warning_management/', include('Warning_management.urls')),
    url(r'^Displacement_management/', include('Displacement_management.urls')),
    url(r'^Dam_Device_management/', include('Dam_Device_management.urls')),
    url(r'^Order_management/', include('Order_management.urls')),
]
