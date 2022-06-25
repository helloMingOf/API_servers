from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.CharField(max_length=25, primary_key=True, verbose_name='用户号')
    name = models.CharField(max_length=25, verbose_name='用户名')
    password = models.CharField(max_length=25, verbose_name='密码')
    region = models.CharField(max_length=25, verbose_name='地址')
    birthday = models.CharField(max_length=25, verbose_name='生日')
    picture = models.ImageField(upload_to='img/',verbose_name='图片路径')
    gender = models.CharField(max_length=10, verbose_name='性别')
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'APP用户信息'
        verbose_name_plural = 'APP用户信息'
    
