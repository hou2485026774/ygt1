"""
@author:houshuai
@software:PyCharm
@time:2021/12/30  17:34
"""
# Create your models here.
from django.db import models
class User(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30,unique=True) #字符串
    spwd = models.CharField(max_length=255)
    #设置生成的表的信息
    class Meta:
        db_table = 'user3'
class Data1(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    citt = models.CharField(max_length=255)