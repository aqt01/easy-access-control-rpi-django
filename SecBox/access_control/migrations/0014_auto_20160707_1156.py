# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 11:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0013_auto_20160707_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorcontroller',
            name='alarm_sound',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 7, 11, 56, 8, 960150), null=True),
        ),
    ]