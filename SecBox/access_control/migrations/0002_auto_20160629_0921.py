# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 09:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensorcontroller',
            name='distance_trigger',
        ),
        migrations.AddField(
            model_name='sensorcontroller',
            name='max_distance',
            field=models.CharField(default=datetime.datetime(2016, 6, 29, 9, 21, 0, 338450), max_length=10, verbose_name=' Max Distance to trigger alarm (cm)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensorcontroller',
            name='min_distance',
            field=models.CharField(default=1, max_length=10, verbose_name='Min Distance to trigger alarm (cm)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 29, 9, 20, 47, 115487)),
        ),
    ]
