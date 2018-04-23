from django.db import models

# Create your models here.
class Carrier(models.Model):
#载体编号
    carrier_num = models.CharField(unique=True,max_length=60)
#名称
    carrier_name = models.CharField(max_length=100)
#载体类型
    carrier_type = models.CharField(max_length=40,default='学员')
#身份编号
    identity_num = models.CharField(max_length=60)
#性别
    sex = models.CharField(max_length=15,default='男')
#出生日期
    birthday = models.DateField()
#民族
    nationality = models.CharField(max_length=50,default='')
#工作单位
    work_unit = models.TextField()
#备注
    remarks = models.TextField()

    def __str__(self):
        return self.carrier_num