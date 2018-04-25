from django.contrib import admin

# Register your models here.
from device_management import models
admin.site.register(models.Device)
admin.site.register(models.DeviceStatus)