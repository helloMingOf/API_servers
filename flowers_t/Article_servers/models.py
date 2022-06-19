from copyreg import pickle
from django.db import models

# Create your models here.
class article(models.Model):
    ID=models.AutoField(primary_key=True,verbose_name='文章ID')
    author=models.CharField(max_length=25,verbose_name='作者名字')
    time=models.CharField(max_length=25,verbose_name='发布时间')
    text=models.TextField(verbose_name='文章内容')
    picture=models.CharField(max_length=100,verbose_name='头像路径')

class flower_book1(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="主键")
    isbn=models.CharField(max_length=40,verbose_name="书编号")
    publishertime=models.CharField(max_length=40,verbose_name="出版时间")
    picture=models.CharField(max_length=100,verbose_name="图片地址")
    bookname=models.CharField(max_length=25,verbose_name="书名")