import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from scripts.play_sound import play_sound
import datetime
from SecBox.settings import BASE_DIR

def run_sensor(sensor_model,sensor_controller):
        import time
        import datetime
        TRIG = 23 
        ECHO = 24

        print "Distance Measurement In Progress"

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIG, False)
        print "Waiting For Sensor To Settle"
        time.sleep(2)


        while 1:
                GPIO.output(TRIG, True)
                time.sleep(0.05)
                GPIO.output(TRIG, False)

                while GPIO.input(ECHO)==0:
                    pulse_start = time.time()

                while GPIO.input(ECHO)==1:
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start

                distance = pulse_duration * 17150

                distance = round(distance, 2)
                #print type(distance)
                #print sensor_controller.objects.all()
                # We register the date and time when the sensor has detected an object
                try:
                        #print 'lol'
                        for i in sensor_controller.objects.all():                            
                            if (distance > i.min_distance and distance < i.max_distance):
                                if (i.capture): 
                                    sensor_object = sensor_model.objects.create(distance=distance,sensor=i)
                                    print i.alarm_sound.url
                                    play_sound(BASE_DIR+'/'+i.alarm_sound.url)
                                    print BASE_DIR+'/'+i.alarm_sound.url
                                #print sensor_object
                                
                                sensor_object.save()
                except:
                    print "Err reading model"                    
              
                print "Distance:",distance,"cm"

        GPIO.cleanup()
