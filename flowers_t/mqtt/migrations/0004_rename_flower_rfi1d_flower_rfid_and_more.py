# Generated by Django 4.0.5 on 2022-06-20 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0003_flower_rfi1d_delete_flower_rfid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='flower_rfi1d',
            new_name='flower_rfid',
        ),
        migrations.RenameField(
            model_name='flower_rfid',
            old_name='time1',
            new_name='time',
        ),
    ]
