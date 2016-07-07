from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class SensorController(models.Model):
    name = models.CharField('name', max_length=80)
    max_distance = models.IntegerField(' Max Distance to trigger alarm (cm)')
    min_distance = models.IntegerField('Min Distance to trigger alarm (cm)')
    alarm_sound = models.FileField(upload_to='media')
    capture = models.BooleanField(default=True)



class SensorData(models.Model):
    date = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    distance = models.FloatField('cm')
    sensor = models.ForeignKey(SensorController)
   
# Create your models here.
