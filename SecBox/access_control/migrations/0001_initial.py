# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 08:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_trigger', models.CharField(max_length=10, verbose_name='Distance to trigger alarm (cm)')),
                ('alarm_sound', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 6, 29, 8, 48, 8, 346854))),
                ('distance', models.CharField(max_length=50)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access_control.SensorController')),
            ],
        ),
    ]
