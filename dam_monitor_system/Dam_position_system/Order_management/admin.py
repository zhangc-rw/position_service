from django.contrib import admin

# Register your models here.
from Order_management import models
admin.site.register(models.Order)
admin.site.register(models.Parameter)