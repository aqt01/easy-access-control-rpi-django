# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 11:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0010_auto_20160629_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='capture',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 7, 11, 18, 53, 78942), null=True),
        ),
    ]
