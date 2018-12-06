from django.db import models
# Create your models here.
class Landing_record(models.Model):
	#计算机名
	Computer_name = models.CharField(max_length=100,null=True)
	#登陆IP
	Computer_ip = models.CharField(max_length=100,null=True)
	#登录时间
	Landing_time = models.DateTimeField(auto_now=True,null=True)
	def __str__(self):
		return self.dam_name
class Dam(models.Model):
	#大坝编号
	dam_num = models.IntegerField(unique=True)
	#大坝名字
	dam_name = models.CharField(max_length=100,null=True)
	#大坝等级
	dam_grade = models.CharField(max_length=100,null=True)
	#大坝概况
	dam_status = models.CharField(max_length=100,null=True)
	#其他信息
	information = models.TextField()
	#端口号
	port_num = models.IntegerField(null=True)
	#域名
	domain_name = models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.dam_name

class Device(models.Model):
	#大坝
	dam = models.ForeignKey(Dam)
	#设备编号
	device_num = models.IntegerField(null=True)
	#设备型号
	card_num = models.CharField(max_length=60,null=True)
	#电池电量
	power = models.FloatField(default=0)
	#标签与设备标识
	at_tip = models.IntegerField(null=True)
	#初始位置坐标
	x = models.FloatField(max_length=60,null=True)
	y = models.FloatField(max_length=60,null=True)
	z = models.FloatField(max_length=60,null=True)
	#距离
	d1 = models.FloatField(null=True)
	d2 = models.FloatField(null=True)
	d3 = models.FloatField(null=True)
	d4 = models.FloatField(null=True)
	#备注
	remark = models.TextField()

	def __str__(self):
		return self.dam.dam_name + " 的 " + str(self.device_num) + " 待测点"

'''class Station_data(models.Model):
	#设备
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
		return self.dam.dam_name + " 的 " + str(self.station_num) + " 锚点"'''


class State_data(models.Model):
	#设备
	device = models.ForeignKey(Device,null=True)
	#警告
	warning = models.IntegerField(null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)
	def __str__(self):
		return self.dam.dam_name + " 的 " + str(self.device_num) + "实时待测点"


class Stationr_data(models.Model):
	#设备
	device = models.ForeignKey(Device,null=True)
	#警告
	warning = models.IntegerField(null=True)
	#更新时间
	dreal_update_time = models.DateTimeField(auto_now=True,null=True)
	#温度
	temperature = models.FloatField(null=True)
	#电压
	voltage = models.FloatField(null=True)

	def __str__(self):
		return self.dam.dam_name + " 的 " + str(self.device_num) + " 历史待测点"

