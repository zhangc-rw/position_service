from django.contrib import admin

# Register your models here.
from Dam_Device_management import models
admin.site.register(models.Dam)
admin.site.register(models.Device)