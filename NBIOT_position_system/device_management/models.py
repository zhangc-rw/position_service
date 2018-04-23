from django.db import models
from carrier_management.models import Carrier

# Create your models here.
class Device(models.Model):
    #设备编号
    device_num = models.CharField(unique=True,max_length=80)
    #设备类型
    device_type = models.CharField(max_length=50)
    #入库时间
    storage_time = models.DateTimeField(auto_now_add=True)
    #更新时间
    update_time = models.DateTimeField(auto_now=True,null=True,)
    #设备卡号
    card_num = models.CharField(max_length=80)
    #关联载体
    associated_carrier = models.ForeignKey(Carrier,null=True,)
    #备注
    remark = models.TextField()

    def __str__(self):
        return self.device_num

class DeviceStatus(models.Model):
    #设备
    device = models.ForeignKey(Device)
    #是否在线
    online = models.BooleanField(default=0)
    #最后在线时间
    last_time = models.DateTimeField(auto_now=True)
    #工作状态
    working_status = models.CharField(max_length=60)
    #电池电量
    power = models.FloatField(default=0)
    #当前业务模式
    business_model = models.CharField(max_length=80)
    #G-Senser激活状态
    G_Senser_state = models.CharField(max_length=80)
    #设备状态
    device_state = models.CharField(max_length=80)

    def __str__(self):
        return self.device.device_num
