from django.db import models
from Dam_Device_management.models import Device
from Dam_Device_management.models import Dam
# Create your models here.
#实时数据
class DReal(models.Model):
	#大坝编号
	#dam = models.ForeignKey(Dam,null=True)
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d1 = models.FloatField(null=True)
	d2 = models.FloatField(null=True)
	d3 = models.FloatField(null=True)
	d4 = models.FloatField(null=True)
	d5 = models.FloatField(null=True)
	d6 = models.FloatField(null=True)
	d7 = models.FloatField(null=True)
	d8 = models.FloatField(null=True)
	#当前位置坐标
	x = models.FloatField(null=True)
	y = models.FloatField(null=True)
	z = models.FloatField(null=True)
	#位移
	d  = models.FloatField(null=True,default=0)
	dx = models.FloatField(null=True,default=0)
	dy = models.FloatField(null=True,default=0)
	dz = models.FloatField(null=True,default=0)

	def __str__(self):
		return str(self.device.dam.dam_num)
#历史数据
class DPast(models.Model):
	#大坝编号
	#dam = models.ForeignKey(Dam,null=True)
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d1 = models.FloatField(null=True)
	d2 = models.FloatField(null=True)
	d3 = models.FloatField(null=True)
	d4 = models.FloatField(null=True)
	d5 = models.FloatField(null=True)
	d6 = models.FloatField(null=True)
	d7 = models.FloatField(null=True)
	d8 = models.FloatField(null=True)
	#当前位置坐标
	x = models.FloatField(null=True)
	y = models.FloatField(null=True)
	z = models.FloatField(null=True)
	#位移
	d = models.FloatField(null=True,default=0)
	dx = models.FloatField(null=True,default=0)
	dy = models.FloatField(null=True,default=0)
	dz = models.FloatField(null=True,default=0)

	def __str__(self):
		return str(self.device.dam.dam_num)

#平滑数据
class Dping(models.Model):
	#大坝编号
	#dam = models.ForeignKey(Dam,null=True)
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d1 = models.FloatField(null=True)
	d2 = models.FloatField(null=True)
	d3 = models.FloatField(null=True)
	d4 = models.FloatField(null=True)
	d5 = models.FloatField(null=True)
	d6 = models.FloatField(null=True)
	d7 = models.FloatField(null=True)
	d8 = models.FloatField(null=True)
	#当前位置坐标
	x = models.FloatField(null=True)
	y = models.FloatField(null=True)
	z = models.FloatField(null=True)
	#位移
	d = models.FloatField(null=True,default=0)
	dx = models.FloatField(null=True,default=0)
	dy = models.FloatField(null=True,default=0)
	dz = models.FloatField(null=True,default=0)

	def __str__(self):
		return str(self.device.dam.dam_num)
#原始数据
class Raw_data(models.Model):
	#大坝编号
	#dam = models.ForeignKey(Dam,null=True)
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#基站编号
	station_num = models.CharField(max_length=60,null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d1 = models.FloatField(null=True)
	d2 = models.FloatField(null=True)
	d3 = models.FloatField(null=True)
	d4 = models.FloatField(null=True)

	def __str__(self):
		return str(self.device.dam.dam_num)
#处理数据
class Processing_data(models.Model):
	#大坝编号
	#dam = models.ForeignKey(Dam,null=True)
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#基站编号
	station_num = models.CharField(max_length=60,null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d = models.FloatField(null=True)

	def __str__(self):
		return str(self.device.dam.dam_num)
#平均数据
class Average_data(models.Model):
	#大坝编号
	#dam = models.ForeignKey(Dam,null=True)
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#基站编号
	station_num = models.CharField(max_length=60,null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d = models.FloatField(null=True)

	def __str__(self):
		return str(self.device.dam.dam_num)
#集合数据
class Convergence_data(models.Model):
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#基站编号
	station_num = models.CharField(max_length=60,null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d = models.FloatField(null=True)

	def __str__(self):
		return str(self.device.dam.dam_num)

#平滑数据
class Smooth_data(models.Model):
	#设备编号
	device = models.ForeignKey(Device,null=True)
	#基站ID
	stationID = models.IntegerField(null=True)
	#基站编号
	station_num = models.CharField(max_length=60,null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	#距离
	d = models.FloatField(null=True)

	def __str__(self):
		return str(self.device.dam.dam_num)