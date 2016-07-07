import os

def play_sound(name):
    os.system('pkill mpg321')
    os.system('mpg321 ' + name + ' &')
