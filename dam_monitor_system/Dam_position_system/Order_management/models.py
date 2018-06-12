from django.db import models
from Dam_Device_management.models import Dam
# Create your models here.
class Order(models.Model):
	#大坝编号
	dam =models.ForeignKey(Dam,null=True)
	#更新时间
	update_time = models.DateTimeField(auto_now=True,null=True)
	#指令类型
	order_type = models.IntegerField(null=True)
	#指令数据
	order_data = models.IntegerField(null=True)
	#基站ID
	stationID = models.CharField(max_length=80,default= '-1',null=True)

	def __str__(self):
		return self.dam.dam_num
		
class Dam_Parameter(models.Model):
	#大坝编号
	dam = models.ForeignKey(Dam,null=True)
	#更新时间
	update_time = models.DateTimeField(auto_now=True,null=True)
	#参数
	parameter_data  = models.IntegerField(null=True)
	'''#参数类型
	parameter_type = models.IntegerField(null=True)
	#参数数据
	parameter_data = models.IntegerField(null=True)'''

	def __str__(self):
		return self.dam.dam_num
