# Generated by Django 4.0.5 on 2022-06-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flower_rfid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('rfid_id', models.CharField(max_length=20, verbose_name='M1卡号')),
                ('flower_name', models.CharField(max_length=20, verbose_name='花名')),
            ],
        ),
    ]
