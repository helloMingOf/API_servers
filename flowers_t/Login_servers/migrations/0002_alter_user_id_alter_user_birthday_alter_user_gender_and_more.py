# Generated by Django 4.0.5 on 2022-06-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_servers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ID',
            field=models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='用户号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(max_length=25, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=25, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=25, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.CharField(max_length=40, verbose_name='图片路径'),
        ),
    ]