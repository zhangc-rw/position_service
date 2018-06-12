from django.db import models
# Create your models here.
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
		return str(self.dam_num)

class Device(models.Model):
	#大坝
	dam = models.ForeignKey(Dam)
	#设备编号
	device_num = models.IntegerField(null=True)
	#设备型号
	card_num = models.CharField(max_length=60,null=True)
	#电池电量
	power = models.FloatField(default=0)
	#初始位置坐标
	x = models.FloatField(max_length=60,null=True)
	y = models.FloatField(max_length=60,null=True)
	z = models.FloatField(max_length=60,null=True)
	#备注
	remark = models.TextField()

	def __str__(self):
		return str(self.dam.dam_num)
