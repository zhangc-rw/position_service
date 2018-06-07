from django.contrib import admin

# Register your models here.
from Displacement_management import models
admin.site.register(models.DReal)
admin.site.register(models.DPast)