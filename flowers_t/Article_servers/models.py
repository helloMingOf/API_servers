from django.db import models

# Create your models here.
class article(models.Model):
    ID=models.AutoField(primary_key=True,verbose_name='文章ID')
    author=models.CharField(max_length=10,verbose_name='作者名字')
    time=models.CharField(max_length=10,verbose_name='发布时间')
    text=models.TextField(verbose_name='文章内容')
    picture=models.CharField(max_length=20,verbose_name='头像路径')