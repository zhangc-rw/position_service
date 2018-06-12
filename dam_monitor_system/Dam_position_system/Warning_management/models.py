from django.db import models
from Dam_Device_management.models import Device
# Create your models here.
class WReal(models.Model):
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.CharField(max_length=80,null=True)
	#更新时间
	wreal_time = models.DateTimeField(auto_now=True,null=True)
	#告警类型
	wreal_type = models.FloatField(null=True)
	#告警标识
	Logo = models.FloatField(null=True)


	def __str__(self):
		return str(self.device.dam.dam_num)

class WPast(models.Model):
	#设备编号
	device= models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.CharField(max_length=80,null=True)
	#更新时间
	wreal_time = models.DateTimeField(auto_now=True,null=True)
	#告警类型
	wreal_type = models.FloatField(null=True)
	#告警标识
	Logo = models.FloatField(null=True)
	
	def __str__(self):
		return str(self.device.dam.dam_num)