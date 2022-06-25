from django.db import models
from django.forms import TimeField

class flower_rfid(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="主键")
    rfid_id=models.CharField(max_length=20,verbose_name="M1卡号")
    time=models.DateTimeField(auto_now_add=True,verbose_name="浇花时间")
    flower_name=models.CharField(max_length=20,verbose_name="花名")
    class Meta:
        db_table = ''
        managed = True
        verbose_name = '浇花信息'
        verbose_name_plural = '浇花信息'

class flower(models.Model):
    id=models.CharField(primary_key=True,max_length=20,verbose_name="卡号")
    flower_name=models.CharField(max_length=20,verbose_name="花名")
    class Meta:
        db_table = ''
        managed = True
        verbose_name = '花名管理'
        verbose_name_plural = '花名管理'