# easy-access-control-rpi-django
Easy access control with django :D Inspired by http://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi 

# NOTES
It runs a script on the background when you run django. All the output it still on the sam screen of the logs of django.

This apps has 2 models

SensorController
- The Sensor controller controls between which distances register the data received from the sensor and assigns a name and an alerts to it (the alert still not working now)

Sensor Data
- Its the stored data received from the sensor which meets the distance between the controlled defined before.




