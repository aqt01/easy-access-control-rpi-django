from django.contrib import admin
from access_control.models import SensorData, SensorController



class SensorControllerAdmin(admin.ModelAdmin):
    list_display = ('max_distance','min_distance', 'alarm_sound')
    
    

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('distance','date','between', 'controller_name')
    def between(self,obj):
        return '%i cm -%i cm'%(obj.sensor.min_distance,obj.sensor.max_distance)
        
    def controller_name(self,obj):
        return '%s' % (obj.sensor.name)
        
    pass


admin.site.register(SensorController,SensorControllerAdmin)
admin.site.register(SensorData,SensorDataAdmin)

# Register your models here.
