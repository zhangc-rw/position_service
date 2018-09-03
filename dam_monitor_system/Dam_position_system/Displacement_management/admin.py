from django.contrib import admin

# Register your models here.
from Displacement_management import models
admin.site.register(models.DReal)
admin.site.register(models.Drping)
admin.site.register(models.Raw_data)

admin.site.register(models.DPast)
admin.site.register(models.DPast_his)
admin.site.register(models.DPast_his_1)
admin.site.register(models.DPast_his_2)
admin.site.register(models.DPast_his_3)

admin.site.register(models.Dping)
admin.site.register(models.Dping_his)
admin.site.register(models.Dping_his_1)
admin.site.register(models.Dping_his_2)
admin.site.register(models.Dping_his_3)

admin.site.register(models.Processing_data)
admin.site.register(models.Processing_data_his)
admin.site.register(models.Processing_data_his_1)
admin.site.register(models.Processing_data_his_2)
admin.site.register(models.Processing_data_his_3)

admin.site.register(models.Average_data)
admin.site.register(models.Average_data_his)
admin.site.register(models.Average_data_his_1)
admin.site.register(models.Average_data_his_2)
admin.site.register(models.Average_data_his_3)

admin.site.register(models.Smooth_data)
admin.site.register(models.Smooth_data_his)
admin.site.register(models.Smooth_data_his_1)
admin.site.register(models.Smooth_data_his_2)
admin.site.register(models.Smooth_data_his_3)

admin.site.register(models.Convergence_data)
admin.site.register(models.Convergence_data_his)
admin.site.register(models.Convergence_data_his_1)
admin.site.register(models.Convergence_data_his_2)
admin.site.register(models.Convergence_data_his_3)

