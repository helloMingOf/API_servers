from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.CharField(max_length=10, primary_key=True, verbose_name='用户号')
    name = models.CharField(max_length=10, verbose_name='用户名')
    password = models.CharField(max_length=10, verbose_name='密码')
    region = models.CharField(max_length=25, verbose_name='地址')
    birthday = models.CharField(max_length=10, verbose_name='生日')
    picture = models.CharField(max_length=20, verbose_name='图片路径')
    gender = models.CharField(max_length=4, verbose_name='性别')