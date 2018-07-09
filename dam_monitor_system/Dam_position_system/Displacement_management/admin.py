from django.contrib import admin

# Register your models here.
from Displacement_management import models
admin.site.register(models.DReal)
admin.site.register(models.DPast)
admin.site.register(models.Raw_data)
admin.site.register(models.Processing_data)
admin.site.register(models.Average_data)