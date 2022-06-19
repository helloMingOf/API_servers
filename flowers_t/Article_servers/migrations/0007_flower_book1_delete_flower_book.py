# Generated by Django 4.0.5 on 2022-06-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article_servers', '0006_flower_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='flower_book1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('isbn', models.CharField(max_length=40, verbose_name='书编号')),
                ('publishertime', models.CharField(max_length=40, verbose_name='出版时间')),
                ('picture', models.CharField(max_length=100, verbose_name='图片地址')),
                ('bookname', models.CharField(max_length=25, verbose_name='书名')),
            ],
        ),
        migrations.DeleteModel(
            name='flower_book',
        ),
    ]
