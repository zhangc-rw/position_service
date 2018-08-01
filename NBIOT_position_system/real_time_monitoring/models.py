from django.db import models
from device_management.models import Device

# Create your models here.
#实时目标信息
class Target(models.Model):
    #设备
    device = models.ForeignKey(Device,null=True)
    #消息接收时间
    update_time = models.DateTimeField(auto_now=True,null=True)
    #运营商消息产生时间
    message_time = models.DateTimeField()
    #工作状态
    working_status = models.CharField(max_length=20)
    #基站编号
    base_num = models.CharField(max_length=80,)
    #小区编号
    cell_num = models.CharField(max_length=80)
    #定位时间
    location_time = models.DateTimeField()
    #当前坐标
    coordinates = models.CharField(max_length=60)
    #速度
    velocity = models.FloatField(default=0)
    #运动方向
    moving_direction = models.FloatField(default=0)
    #高度
    height = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.device.associated_carrier.carrier_num)
#历史目标信息
class Past_Target(models.Model):
    #设备
    device = models.ForeignKey(Device,null=True)
    #消息接收时间
    update_time = models.DateTimeField(auto_now=True,null=True)
    #运营商消息产生时间
    message_time = models.DateTimeField()
    #工作状态
    working_status = models.CharField(max_length=20)
    #基站编号
    base_num = models.CharField(max_length=80,)
    #小区编号
    cell_num = models.CharField(max_length=80)
    #定位时间
    location_time = models.DateTimeField()
    #当前坐标
    coordinates = models.CharField(max_length=60)
    #速度
    velocity = models.FloatField(default=0)
    #运动方向
    moving_direction = models.FloatField(default=0)
    #高度
    height = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.device.associated_carrier.carrier_num)
