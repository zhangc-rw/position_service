from django.contrib import admin

# Register your models here.
from real_time_monitoring import models
admin.site.register(models.Target)
