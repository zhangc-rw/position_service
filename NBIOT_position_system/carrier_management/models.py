from django.db import models

# Create your models here.
class Carrier(models.Model):
#载体编号
    carrier_num = models.IntegerField(unique=True)
#名称
    carrier_name = models.CharField(max_length=100)
#载体类型
    carrier_type = models.IntegerField()
#身份编号
    identity_num = models.IntegerField(null=True)
#性别
    sex = models.CharField(max_length=15,null=True)
#出生日期
    birthday = models.DateField()
#民族
    nationality = models.CharField(max_length=50,null=True)
#工作单位
    work_unit = models.TextField(null=True)
#备注
    remarks = models.TextField(null=True)

    def __str__(self):
        return self.carrier_num