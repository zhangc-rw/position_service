from django.contrib import admin

# Register your models here.
from Warning_management import models
admin.site.register(models.WReal)
admin.site.register(models.WPast)