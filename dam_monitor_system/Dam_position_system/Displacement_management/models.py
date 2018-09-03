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
		return self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的实时数据" 

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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "
#历史数据_his
class DPast_his(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "
#历史数据_his_1
class DPast_his_1(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "
#历史数据_his_2
class DPast_his_2(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "
#历史数据_his_3
class DPast_his_3(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "

#平滑数据实时显示 
class Drping(models.Model):
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
		return self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的实时数据" 


#平滑数据历史显示
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "

#平滑数据历史显示_his
class Dping_his(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "
#平滑数据历史显示_his_1
class Dping_his_1(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "
#平滑数据历史显示_his_2
class Dping_his_2(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "
#平滑数据历史显示_his_3
class Dping_his_3(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点的数据 "

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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#处理数据
class Processing_data_his(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#处理数据
class Processing_data_his_1(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#处理数据
class Processing_data_his_2(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#处理数据
class Processing_data_his_3(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"


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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"


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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#平均数据_his
class Average_data_his(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#平均数据_his_1
class Average_data_his_1(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#平均数据_his_2
class Average_data_his_2(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#平均数据_his_3
class Average_data_his_3(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"



#收敛数据
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#收敛数据_his
class Convergence_data_his(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#收敛数据_his_1
class Convergence_data_his_1(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#收敛数据_his_2
class Convergence_data_his_2(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#收敛数据_his_3
class Convergence_data_his_3(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"


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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"

#平滑数据_his
class Smooth_data_his(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#平滑数据_his_1
class Smooth_data_his_1(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#平滑数据_his_2
class Smooth_data_his_2(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"
#平滑数据_his_3
class Smooth_data_his_3(models.Model):
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
		return str(self.id) + " 流水号 " + self.device.dam.dam_name + " 的 " + str(self.device.device_num) + " 待测点与 " + str(self.stationID) + " 锚点间的数据"

